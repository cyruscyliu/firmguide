# Salamander

[![CircleCI](https://circleci.com/gh/cyruscyliu/esv/tree/master.svg?style=svg&circle-token=7f12caaa351d02731d57d8165e634dc3e3537d33)](https://circleci.com/gh/cyruscyliu/esv/tree/master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a7aacb11a3b14a7d8e069d8a440a43c0)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=cyruscyliu/esv&amp;utm_campaign=Badge_Grade)

Firmware analysis matters in embedded system security, especially dynamic firmware analysis which can
discover deep and complicated vulnerabilities. However, we cannot do dynamic firmware analysis immediately
because of lack of virtual execution environment. Salamander is such a project that builds the virtual
execution environment in a pure software way, showing us a feasible way to boot up any firmware in
limited steps, which is of scale and reliable. In this very early stage, Salamander only targets Linux-based
firmware and can only be used standalone.

## Install

```shell script
git clone https://github.com/cyruscyliu/esv.git salamander && \
    cd salamander && mkdir ~/build && ./setup.sh
```

## Usage

Step 1, create a project. Salamander is a project-style tool. A project is a global information
center and will be used in every future step implicitly. The project is quite useful saving you
from long and forgettable command lines. See `./salamander create -h` for help to create a project.

Step 2, analyze your source. Salamander is a command-style tool. Salamander has three groups of
commands, core, plugins, settings. It is very simple to analyze your source if you've already create a project.

```
./salamander analyze
./salamander declare
```

Step 3, diagnose your model. Salamander is a config-style tool. The world of embedded systems is
full of fragmentation such that Salamander must be unchangeable to new models. We make all models
as configs, which all commands reading/writing  with a set of universal interfaces. We've built in
several models and once you've got a firmware with device tree, mostly, you will be working on your
own models, ICT modeling and IV resolving. It takes time to try and try again to finally get precise
models. Salamander has a QEMU debugging interface and some plugins to help your jobs.


```
./salamander batch -c 1 -e dir/to/images
./salamander -d diagnose
```

Step 4, boot up firmware. Salamander is a full solution from modeling to booting. We can boot up
firmware not only compiled with source but also scratched in the wild. Enjoy your time!

```
./salamander boot -f path/to/image
```

## Contributors
[cyruscyliu*](https://github.com/cyruscyliu/esv), [occia*](https://github.com/occia)

## License
[MIT License](./LICENSE)

