class JustANode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                    "image": ("IMAGE", ),
                    "filepath": ("FILEPATH", ),
            },
        }
    RETURN_TYPES = ("IMAGEUPLOAD",)
    FUNCTION = "save_image"

    CATEGORY = "loaders"

    def save_image(self, image, filepath):
        return image


NODE_CLASS_MAPPINGS = {
    "JustANode": JustANode,
}
