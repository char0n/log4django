
def exception_callback_print(ex, gaerman_worker=None):
    """Prints exceptions and do nothing else."""
    print ex


def exception_callback_shutdown(ex, gearman_worker=None):
    """Prints exception and exits the worker loop."""
    exception_callback_print(ex)
    gearman_worker.shutdown()