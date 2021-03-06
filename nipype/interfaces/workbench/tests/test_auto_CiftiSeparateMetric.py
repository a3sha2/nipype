# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..cifti import CiftiSeparateMetric


def test_CiftiSeparateMetric_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        direction=dict(
            argstr="%s ",
            mandatory=True,
            position=1,
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr="%s ",
            extensions=None,
            mandatory=True,
            position=0,
        ),
        metric=dict(
            argstr=" -metric %s ",
            mandatory=True,
            position=2,
        ),
        out_file=dict(
            argstr=" %s",
            extensions=None,
            keep_extension=True,
            name_source=["in_file"],
            name_template="correlation_matrix_%s.func.gii",
            position=3,
        ),
    )
    inputs = CiftiSeparateMetric.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_CiftiSeparateMetric_outputs():
    output_map = dict(
        out_file=dict(
            extensions=None,
        ),
    )
    outputs = CiftiSeparateMetric.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
