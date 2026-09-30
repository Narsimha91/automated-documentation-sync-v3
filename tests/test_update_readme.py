from src.features import FEATURES, features


def test_features_are_available() -> None:
    feature_list = features()

    assert isinstance(feature_list, list)
    for feature in FEATURES:
        assert feature in feature_list