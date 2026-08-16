This directory is the raw reFrame results directory for the results in the 
paper. These results also contain significant results that were not part of
the paper - for example, due to errors in runs or being part of early 
experiments. Unfortunately, reFrame doesn't have a simple way to export 
only portions of the results directory.

reFrame also unfortunately does not allow adjusitng tags after the fact on 
tests. Some of these filters are, unfortnately, fairly complicated as the 
tagging system evolved over the course of the experiments. Due to time 
constraints, we were neither able to rerun the experiments for new tags, nor 
re-write the Jupyter notebooks to compensate. This will likely be a future
improvement.

# Filters

When reproducing the results using the Jupyter notebooks, the following are the
filters in use. These are the second half of the filter expression, after the 
`test==...` portion. So If this says:

`and benchmark==\"sp\"`

the full filter condition would be:

`test==\"no_monitoring\" and benchmark==\"sp\"`

This adjustment should be made for `baseline_query` and `experimental_queries`
in PilotStudy.ipynb and `tag_baseline` and `tags_varying`.

## `sp`

`and benchmark==\"sp\"`

## `hpl`

`and benchmark==\"hpl\"`

HPL also has a separate baseline for the "BMC without `amsd`" test, and the 
`test` parameter of the `baseline` filter should be changed to 
`test==\"no_monitoring_bmc_only\"`

## EP size E

`and (\"jobsize\" not in locals() or jobsize==\"E\") and (\"benchmark\" not in locals() or benchmark==\"ep\")`

EP size E also has a separate baseline for the "BMC without `amsd`" test, and the 
`test` parameter of the `baseline` filter should be changed to 
`test==\"no_monitoring_bmc_only\"`

## EP size D

`jobsize==\"D\" and (\"benchmark\" not in locals() or benchmark==\"ep\")`

EP size D also has a separate baseline for the "BMC without `amsd`" test, and the 
`test` parameter of the `baseline` filter should be changed to 
`test==\"no_monitoring_bmc_only\"`