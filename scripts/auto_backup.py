import os.path
import gradio as gr
import modules.scripts as scripts
import sys
import configparser


from modules.shared import opts
base_dir = scripts.basedir()
sys.path.append(base_dir)


config_path = os.path.join(base_dir, 'user-config.cfg')


def make_missing_directory_and_parent(destination_directory):
    parent_directory = os.path.dirname(destination_directory)
    if not os.path.exists(parent_directory):
        parent_directory = os.path.dirname(destination_directory)
        os.mkdir(parent_directory)
    os.mkdir(destination_directory)


def save_images_to_directory(images, backup_directory):
    for image in images:
        full_destination = os.path.join(backup_directory, image.already_saved_as)
        destination_directory = os.path.dirname(full_destination)
        if not os.path.exists(destination_directory):
            make_missing_directory_and_parent(destination_directory)
        image.save(full_destination)
        print('saved "\033[94m' + os.path.basename(full_destination) + '\033[0m" to "\033[94m' + os.path.dirname(full_destination) + '\033[0m"')


class AutoBackupScript(scripts.Script):
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(config_path)
        self.initial_sd_backup_paths = self.config['PATHS']['backup_paths']

    def title(self):
        return "Auto-backup"

    def ui(self, is_img2img):
        backup_folder_textbox = gr.Textbox(value=lambda: self.initial_sd_backup_paths, label='Backup folders', interactive=True)
        return [backup_folder_textbox]

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def postprocess(self, p, res, *args):
        with open(config_path, 'w') as config_file:
            self.config['PATHS']['backup_paths'] = args[0]
            self.config.write(config_file)

        save_paths = args[0].split('|')
        if opts.samples_save and not p.do_not_save_samples:
            for save_path in save_paths:
                save_path = save_path.strip()
                if save_path == '':
                    continue
                save_images_to_directory(res.images, save_path)
