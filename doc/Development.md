Table of Contents
=================

   * [Development](#development)
      * [Add analysis (group)](#add-analysis-group)
      * [APIs for analysis (group)](#apis-for-analysis-group)
         * [Analysis Manager](#analysis-manager)
         * [Frimware profile getter/setter](#frimware-profile-gettersetter)
         * [Components getter/setter](#components-gettersetter)
         * [Device tree parsers (dt_parsers)](#device-tree-parsers-dt_parsers)
         * [Database](#database)
         * [QEMU controller](#qemu-controller)
         * [Source controller](#source-controller)
      * [Add subcommand](#add-subcommand)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)

# Development

## Add analysis (group)

An analysis focuses on a specific task, such as parsing a device tree blob,
which is the basic schedule unit in FirmGuide. Each analysis is a Python
class and all of them are put under `slcore/analysis`.
Several analyses work together as an analysis group that is more powerful
to accomplish a complex task. The group of analysis is defined in `slcore/aconfigs`.

Here is the template of an analysis.
```Python
# slcore/analyses/analysis_name.py
from slcore.amanager import Analysis

class AnalysisClassName(Analysis):
      def __init__(self, analysis_manager):
         super().__init__(analysis_manager)
         self.name = 'analysis_name'
         self.description = 'analysis description'
         self.required = []  # what other analysis that should be executed in advance

      def run(self):
         return True
```

Here is an example of the analysis group definition.

```yaml
# touch slcore/aconfigs/plugins/xxx.a.yaml
AnalysisGroupClassName:
   analyses: [AnalysisClassName1, AnalysisClassName2, AnalysisClassName3]
   description: 'analysis group description'
```

## APIs for analysis (group)

### Analysis Manager

```python
def run(self, **kwargs):
    # get details of the project
    self.analysis_manager.project.attrs['path']
    self.analysis_manager.project.attrs['base_dir']
    # log
    self.warning('message', 1)
    self.info('message', 1)
    self.debug('message', 1)
    # return False after setting an error information
    if False:
