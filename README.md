# wfork-streamlit-profiler &nbsp;🏄🏼

[![PyPi](https://img.shields.io/pypi/v/wfork-streamlit-profiler)](https://pypi.org/project/wfork-streamlit-profiler/)

**Runtime profiler for Streamlit, powered by [pyinstrument](https://github.com/joerick/pyinstrument).**

*wfork-streamlit-profiler is a fork of streamlit-profiler 0.2.4. If there are any newer versions of the original streamlit-profiler, you should probably use those instead. See the original project's github for more: https://github.com/jrieke/streamlit-profiler*

streamlit-profiler is a [Streamlit component](https://streamlit.io/components) that
helps you find out which parts of your app are slow. It profiles the code via
[pyinstrument](https://github.com/joerick/pyinstrument) and shows the results right
within your Streamlit app.

---

<h3 align="center">
  ⏱️ <a href="https://share.streamlit.io/jrieke/streamlit-profiler/main/examples/basic.py">Live demo</a> ⏱️
</h3>

---

<p align="center">
    <a href="https://share.streamlit.io/jrieke/streamlit-profiler/main/examples/basic.py"><img src="images/demo.png" width=600></a>
</p>

## Installation

```bash
pip install wfork-streamlit-profiler
```

## Usage

```python3
import streamlit as st
from wfork_streamlit_profiler import Profiler

with Profiler():
    st.title("My app")
    # ... other code
```

Or:
```python3
import streamlit as st
from wfork_streamlit_profiler import Profiler

p = Profiler()
p.start()
# ... other code
p.stop()
```

Then start your app as usual: `streamlit run my_app.py`

The `Profiler` class is an extension of `pyinstrument.Profiler`, so you can use
[all of its functions](https://pyinstrument.readthedocs.io/en/latest/reference.html#pyinstrument.Profiler).

Don't want the profiler to immediately display when you stop profiling? Initialize it with `Profiler(auto_output_on_stop=False)` instead, and call the `.output_streamlit()` method whenever you want it to display, instead. You can also set the async_mode of the profiler in the pyinstrument in the same constructor, whatever that means.
