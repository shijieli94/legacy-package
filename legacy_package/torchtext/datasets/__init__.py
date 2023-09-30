from .babi import BABI20
from .imdb import IMDB
from .language_modeling import (
    LanguageModelingDataset,
    PennTreebank,
    WikiText2,
    WikiText103,
)
from .nli import SNLI, XNLI, MultiNLI
from .sequence_tagging import UDPOS, CoNLL2000Chunking, SequenceTaggingDataset
from .sst import SST
from .text_classification import (
    AG_NEWS,
    AmazonReviewFull,
    AmazonReviewPolarity,
    DBpedia,
    SogouNews,
    TextClassificationDataset,
    YahooAnswers,
    YelpReviewFull,
    YelpReviewPolarity,
)
from .translation import IWSLT, WMT14, Multi30k, TranslationDataset
from .trec import TREC
from .unsupervised_learning import EnWik9

__all__ = [
    "BABI20",
    "IMDB",
    "LanguageModelingDataset",
    "PennTreebank",
    "WikiText2",
    "WikiText103",
    "SNLI",
    "XNLI",
    "MultiNLI",
    "UDPOS",
    "CoNLL2000Chunking",
    "SequenceTaggingDataset",
    "SST",
    "AG_NEWS",
    "AmazonReviewFull",
    "AmazonReviewPolarity",
    "DBpedia",
    "SogouNews",
    "TextClassificationDataset",
    "YahooAnswers",
    "YelpReviewFull",
    "YelpReviewPolarity",
    "IWSLT",
    "WMT14",
    "Multi30k",
    "TranslationDataset",
    "TREC",
    "EnWik9",
]
