import _plotly_utils.basevalidators


class ZerolinecolorValidator(_plotly_utils.basevalidators.ColorValidator):

    def __init__(
        self,
        plotly_name='zerolinecolor',
        parent_name='layout.scene.xaxis',
        **kwargs
    ):
        super(ZerolinecolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            role='style',
            **kwargs
        )