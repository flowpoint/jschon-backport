import pathlib

from jschon.keywords.applicator import *
from jschon.keywords.validation import *
from jschon.schema import Metaschema, Vocabulary

Metaschema.register(
    uri="https://json-schema.org/draft/2019-09/schema",
    filepath=pathlib.Path(__file__).parent / 'catalogue' / 'jsonschema_201909' / 'schema',
)

Vocabulary.register(
    uri="https://json-schema.org/draft/2019-09/vocab/core",
    kwclasses=()
)

Vocabulary.register(
    uri="https://json-schema.org/draft/2019-09/vocab/applicator",
    kwclasses=(
        AllOfKeyword,
        AnyOfKeyword,
        OneOfKeyword,
        NotKeyword,
        IfKeyword,
        ThenKeyword,
        ElseKeyword,
        DependentSchemasKeyword,
        ItemsKeyword,
        AdditionalItemsKeyword,
        UnevaluatedItemsKeyword,
        ContainsKeyword,
        PropertiesKeyword,
        PatternPropertiesKeyword,
        AdditionalPropertiesKeyword,
        UnevaluatedPropertiesKeyword,
        PropertyNamesKeyword,
    )
)

Vocabulary.register(
    uri="https://json-schema.org/draft/2019-09/vocab/validation",
    kwclasses=(
        TypeKeyword,
        EnumKeyword,
        ConstKeyword,
        MultipleOfKeyword,
        MaximumKeyword,
        ExclusiveMaximumKeyword,
        MinimumKeyword,
        ExclusiveMinimumKeyword,
        MaxLengthKeyword,
        MinLengthKeyword,
        PatternKeyword,
        MaxItemsKeyword,
        MinItemsKeyword,
        UniqueItemsKeyword,
        MaxContainsKeyword,
        MinContainsKeyword,
        MaxPropertiesKeyword,
        MinPropertiesKeyword,
        RequiredKeyword,
        DependentRequiredKeyword,
    )
)

Vocabulary.register(
    uri="https://json-schema.org/draft/2019-09/vocab/meta-data",
    kwclasses=()
)

Vocabulary.register(
    uri="https://json-schema.org/draft/2019-09/vocab/format",
    kwclasses=()
)

Vocabulary.register(
    uri="https://json-schema.org/draft/2019-09/vocab/content",
    kwclasses=()
)
