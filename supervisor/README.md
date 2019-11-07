# supervisor

This is a supervisor that manages and controls whole system.

## tasks

Provided we have a firmware blob and its source code, we are going to perform tasks below.

1. static inference to get `path_to_` properties and `string_to_` properties
2. device profile generation using `path_to_` `string_to_` `initial_value_to` properties
3. QEMU code generation through the device profile
4. execution trace collection for 5 minutes
5. dynamic policy checking to evaluate the profile quality, if good, then exit
6. dynamic inference to get`initial_value_to` properties
7. go 2