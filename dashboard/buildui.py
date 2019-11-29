import pandas as pd
import re
import numpy as np
from collections import OrderedDict
from pyxley.charts.datatables import DataTable
from pyxley import UILayout, register_layouts

import json


def get_data(filename="databoard/data.json"):
    df = pd.DataFrame(json.load(open(filename, "r")))
    df = df.dropna()

    return df


def create_datatable(df, tablename="salamander"):
    cols = OrderedDict([
        ("uuid", {"label": "firmware uuid"}),
        ("analysis", {"label": "analysis count"}),
        ("saved", {"label": "saved"}),
    ])

    _table = DataTable(tablename, "/api/{}/".format(tablename), df,
                       columns=cols, paging=True, pageLength=9, scrollX=True,
                       columnDefs=[{
                           "render": """<svg width="156" height="20"><g></g></svg>""",
                           "orderable": False,
                           "targets": 3
                       }],
                       sDom='<"top">rt<"bottom"lp><"clear">', deferRender=True,
                       )

    return _table


def make_table_layout(filename):
    df = get_data(filename)

    ui = UILayout("SimpleChart")
    ui.add_chart(create_datatable(df))
    return ui


def get_layouts(mod, filename):
    dt_ui = make_table_layout(filename)
    dt_ui.assign_routes(mod)
    dt_props = dt_ui.build_props()

    _layouts = {
        "datatable": {"layout": [dt_props], "title": "SALAMANDER"}
    }
    register_layouts(_layouts, mod)
