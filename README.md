# STATEMENT
* This is a modified version of code in https://github.com/paparazzi/paparazzi. Our purpose is to modify the codebase of paparazzi so that we could apply our static code analysis tool on it (https://github.com/Bounding-Function-Artifacts-OOPSLA-2020/PBF-Detector). This repository is intended for research purpose.

# NOTES
* 'change_log.txt' shows the change on paparazzi codebase since 10/8/2019.
* 'modify_plugin_path_list.txt' shows places where we need the path of the Bounding Function dictionary builder clang plugin. This plugin 'BFDictBuilderPlugin.so' is provided in the static code analysis tool repository (https://github.com/Bounding-Function-Artifacts-OOPSLA-2020/PBF-Detector). Please pull that git repository to your computer and refer to 'modify_plugin_path_list.txt' to replace the plugin paths. 