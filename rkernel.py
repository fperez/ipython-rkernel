"""A "native" IPython R kernel in 15 lines of code.

This isn't a real native R kernel, just a quick and dirty hack to get the
basics running in a few lines of code.

Put this into your startup directory for a profile named 'rkernel' or somesuch,
and upon startup, the kernel will imitate an R one by simply prepending `%%R`
to every cell.
"""

from IPython.core.interactiveshell import InteractiveShell

print '*** Initializing R Kernel ***'
ip = get_ipython()
ip.run_line_magic('load_ext', 'rmagic')
ip.run_line_magic('config', 'Application.verbose_crash=True')

old_run_cell = InteractiveShell.run_cell

def run_cell(self, raw_cell, **kw):
    return old_run_cell(self, '%%R\n' + raw_cell, **kw)

InteractiveShell.run_cell = run_cell
