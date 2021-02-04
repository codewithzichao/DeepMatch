import tensorflow as tf
from tensorflow.python.keras import backend as K

from deepmatch.models import NARM
from deepmatch.utils import sampledsoftmaxloss
from tests.utils import check_model,get_xy_fd_narm


def test_NARM():
    model_name = "NARM"

    x, y, user_feature_columns, item_feature_columns = get_xy_fd_narm(False)
    K.set_learning_phase(True)

    if tf.__version__ >= '2.0.0':
        tf.compat.v1.disable_eager_execution()

    model=NARM(user_feature_columns,item_feature_columns,num_sampled=2)
    model.compile('adam', sampledsoftmaxloss)

    check_model(model, model_name, x, y, check_model_io=True)


if __name__ == "__main__":
    test_NARM()
