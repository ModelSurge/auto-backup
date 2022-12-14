# auto-backup
An automatic1111 webui extension to save your image generations on other locations on your machine simultaneously. 

## Installation
1. Visit the **Extensions** tab of Automatic's WebUI.
2. Visit the **Install from URL** subtab.
3. Copy and paste `https://github.com/auto-webui-extensions-and-scripts/auto-backup` in the **URL for extension's git repository** textbox.
4. Press the **Install** button. 


## Usage
Just specify in the `Backup folders` the additional paths to save the images to.  
You can ask for multiple paths at once by separating them with a pipe (`|`).  
For example, if I want to save the images on 2 different drives, `D` and `F`, I can write this in the textbox:  
`D:\my\stable diffusion\backup\folder | F:\my other\stable diffusion\backup\folder`  

If you don't write any path, it won't save additional images at all.  
This extension does not override the default behaviour of the webui. If you have the `Always save all generated images` checkbox checked in the webui settings, you will still be saving them on your hard-drive at the specified path in the settings.
