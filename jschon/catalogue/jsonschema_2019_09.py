import submodules
from jschon.catalogue import Catalogue
from jschon.jsonschema import *
from jschon.keywords import *
from jschon.uri import URI
from jschon.vocabulary.core import *


def initialize():
    JSONSchema.bootstrap(
        IdKeyword,
        SchemaKeyword,
        VocabularyKeyword,
    )

    Catalogue.add_directory(
        base_uri=URI('https://json-schema.org/draft/2019-09/'),
        base_dir=submodules.rootdir / 'json-schema-spec-2019-09',
    )

    Catalogue.create_vocabulary(
        URI("https://json-schema.org/draft/2019-09/vocab/core"),
        SchemaKeyword,
        VocabularyKeyword,
        IdKeyword,
        RefKeyword,
        AnchorKeyword,
        RecursiveRefKeyword,
        RecursiveAnchorKeyword,
        DefsKeyword,
        CommentKeyword,
    )

    Catalogue.create_vocabulary(
        URI("https://json-schema.org/draft/2019-09/vocab/applicator"),
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

    Catalogue.create_vocabulary(
        URI("https://json-schema.org/draft/2019-09/vocab/validation"),
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

    Catalogue.create_vocabulary(
        URI("https://json-schema.org/draft/2019-09/vocab/format"),
        FormatKeyword,
    )

    Catalogue.create_vocabulary(
        URI("https://json-schema.org/draft/2019-09/vocab/meta-data"),
        TitleKeyword,
        DescriptionKeyword,
        DefaultKeyword,
        DeprecatedKeyword,
        ReadOnlyKeyword,
        WriteOnlyKeyword,
        ExamplesKeyword,
    )

    Catalogue.create_vocabulary(
        URI("https://json-schema.org/draft/2019-09/vocab/content"),
        ContentMediaTypeKeyword,
        ContentEncodingKeyword,
        ContentSchemaKeyword,
    )

    # cache and self-validate the metaschema and its vocabularies
    metaschema_uri = URI("https://json-schema.org/draft/2019-09/schema")
    metaschema = JSONSchema.load(metaschema_uri, metaschema_uri=metaschema_uri)
    metaschema.validate()
