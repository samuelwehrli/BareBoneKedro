import os
from kedro.io import AbstractDataset
import pandas as pd

# === HDF5 Dataset  ==============================================
class HDF5Dataset(AbstractDataset):
    """A custom dataset for loading hdf5 files.

    Allows to pass in additional arguments to the `scipy.io.loadmat` function.
    """
    def __init__(self, filepath: str, key = 'data'):
        self._filepath = filepath
        self._key = key

    def _load(self, start = None, stop = None) -> pd.DataFrame:
        # overwrite so that dataframe is returned
        return pd.read_hdf(self._filepath, key=self._key, start=start, stop=stop)

    def _save(self, data: pd.DataFrame) -> None:
        # save data to hdf5 file
        os.makedirs(os.path.dirname(self._filepath), exist_ok=True)
        data.to_hdf(self._filepath, key=self._key)

    def _exists(self) -> bool:
        return os.path.exists(self._filepath)

    def _describe(self) -> dict:
        return dict(filepath=self._filepath)

