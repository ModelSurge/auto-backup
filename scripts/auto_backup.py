import os.path
import gradio as gr
import modules.scripts as scripts
import sys
import configparser


from modules.shared import opts
base_dir = scripts.basedir()
sys.path.append(base_dir)


config_path = os.path.join(base_dir, 'user-config.cfg')

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
                for image in res.images:
                    save_path = save_path.strip()
                    if save_path == '':
                        continue
                    save_path = os.path.join(save_path, image.already_saved_as)
                    if not os.path.exists(os.path.dirname(save_path)):
                        dir_to_make = os.path.dirname(save_path)
                        if not os.path.exists(dir_to_make):
                            root_dir_to_make = os.path.dirname(dir_to_make)
                            os.mkdir(root_dir_to_make)
                        os.mkdir(dir_to_make)
                    image.save(save_path)
                    print('saved "\033[94m' + os.path.basename(save_path) + '\033[0m" to "\033[94m' + os.path.dirname(save_path) + '\033[0m"')
