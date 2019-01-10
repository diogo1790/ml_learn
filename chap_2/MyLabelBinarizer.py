from sklearn.base import TransformerMixin #gives fit_transform method for free
from sklearn.preprocessing import LabelBinarizer

class MyLabelBinarizer(TransformerMixin):
    def __init__(self, *args, **kwargs):
        self.encoder = LabelBinarizer(*args, **kwargs)
		
    def fit(self, x, y=0):
        self.encoder.fit(x)
        return self
		
    def transform(self, x, y=0):
        return self.encoder.transform(x)