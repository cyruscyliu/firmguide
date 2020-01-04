# Analysis

### Programming Model

#### Analysis

All analysis except `Analysis Group` must extend `Analysis` and set its `name`, `description`, 
`log_suffix`, `required`, and `context hint`. 
+ `name` the identification of an analysis which should be universal unique
+ `description` the description of the analysis which helps debug
+ `required` **the names of analyses which must be run before this analysis**
+ `context hint` the exception hint for this analysis which helps debug
+ and put more specific requirement in `context input` to solve the exception
+ `critical` if an analysis is critical and it fails, the whole program stops

#### Analysis Worker

Sub-analyses run in order. Not declared explicitly.

#### Analysis Group

[WIP] Multiple analyses as a group but only one is valid.
Extend `AnalysisGroup` in stead of `Analysis`.

#### Analysis Manager

Call `register_analysis` to register an analysis and call `run` to run them all. 
The details are transparent to developers and all analyses will be run in topology
order according to their requirements.

### Built-in Analysis
[analyses.csv](./.analyses.csv)
