import pytest
from dash.testing.application_runners import import_app

# Load your Dash app
@pytest.fixture
def dash_app():
    app = import_app("DataVisualisationWithRadioButtn_Solution")  # default looks for `app`
    return app



# 1. Test that the header is present
def test_header_is_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)

    header = dash_duo.find_element("#header")
    assert header is not None
    assert "Pink Morsel Visualizer" in header.text


# 2. Test that the visualization (graph) is present
def test_visualization_is_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)

    graph = dash_duo.find_element("#visualization")
    assert graph is not None


# 3. Test that the region picker is present
def test_region_picker_is_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)

    picker = dash_duo.find_element("#region_picker")
    assert picker is not None
