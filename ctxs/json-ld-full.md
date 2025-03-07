# JSON-LD 1.1

> JSON-LD 1.1 is a JSON-based format to serialize Linked Data. The syntax is designed to easily integrate into deployed systems already using JSON, and provides a smooth upgrade path from JSON to JSON-LD. It allows expressing directed graphs, where nodes can be identified using IRIs, enabling data to be linked across different documents or websites.

JSON-LD stands for JavaScript Object Notation for Linked Data. It's a method to encode Linked Data using JSON. JSON-LD is primarily intended to be a way to use Linked Data in web-based programming environments, to build interoperable web services, and to store Linked Data in JSON-based storage engines.

JSON-LD 1.1 is a superset of the features defined in JSON-LD 1.0 and, except where noted, documents created using the 1.0 version remain compatible with JSON-LD 1.1.

Key features include:
- Universal identifier mechanism for JSON objects via IRIs
- Ways to disambiguate properties and values with contexts
- A mechanism to refer to values in other documents
- Language and datatype support for values
- A way to express multiple relationships in a single document

## Core Concepts

- [The Context](https://www.w3.org/TR/json-ld11/#the-context): The context in JSON-LD allows for shortening IRIs to terms and simplifying the structure by mapping terms to IRIs. It enables the conversion of a JSON document to a JSON-LD document without requiring significant changes, providing interoperability. Context can be embedded directly in a JSON-LD document or referenced from an external source. A context definition must be valid JSON/JSON-LD, and keywords like `@context`, `@id`, and `@type` have specific roles in defining how properties and values are processed.

- [IRIs](https://www.w3.org/TR/json-ld11/#iris): IRIs (Internationalized Resource Identifiers) are used in JSON-LD to uniquely identify nodes and properties. They can be represented as absolute IRIs, relative IRI references, compact IRIs (using prefixes), or terms defined in the context. IRIs provide the foundation for linked data by enabling references to resources across documents and websites.

- [Node Identifiers](https://www.w3.org/TR/json-ld11/#node-identifiers): In JSON-LD, nodes can be identified using the `@id` keyword with an IRI or blank node identifier. This allows for referencing the node from other parts of the document or from external documents. Blank node identifiers begin with "_:" and are used for nodes without a specific IRI.

- [Types](https://www.w3.org/TR/json-ld11/#specifying-the-type): The `@type` keyword is used to specify the type of a node or a value. For nodes, it indicates the class or classes that the node belongs to. For values, it provides datatype information such as xsd:dateTime or xsd:integer.

- [Values](https://www.w3.org/TR/json-ld11/#describing-values): JSON-LD distinguishes between node objects and value objects. Value objects are represented using the `@value` key and can be associated with a type using `@type`, a language using `@language`, or a direction using `@direction`. This enables the representation of typed values, language-tagged strings, and strings with directional information.

- [Lists and Sets](https://www.w3.org/TR/json-ld11/#lists-and-sets): JSON-LD provides mechanisms for representing ordered collections (lists) and unordered collections (sets). Lists are represented using the `@list` keyword, while sets can be expressed using the `@set` keyword or as regular JSON arrays. The `@container` keyword in a term definition can specify that values should be treated as lists or sets.

- [Nested Properties](https://www.w3.org/TR/json-ld11/#nested-properties): Nested properties allow for grouping related properties within a node object using the `@nest` keyword. This provides a way to organize data without affecting the semantics of the graph.

- [Embedding](https://www.w3.org/TR/json-ld11/#embedding): JSON-LD supports embedding node objects within other node objects, creating a parent-child relationship. This allows for representing complex data structures in a natural way without requiring explicit node identifiers for every node.

- [Indexed Values](https://www.w3.org/TR/json-ld11/#indexed-values): JSON-LD provides mechanisms for indexing values by property, language, identifier, or type. This enables efficient access to specific values within a collection without having to scan through an array.

- [Reverse Properties](https://www.w3.org/TR/json-ld11/#reverse-properties): The `@reverse` keyword allows for expressing relationships in the reverse direction. This is useful when the natural direction of a relationship is from the object to the subject rather than from the subject to the object.

- [Named Graphs](https://www.w3.org/TR/json-ld11/#named-graphs): JSON-LD supports named graphs, which are collections of statements with an associated graph name. Named graphs are expressed using the `@graph` keyword in combination with `@id` for the graph name. This allows for making statements about statements and for organizing data into distinct subgraphs.

## Document Forms

- [Expanded Document Form](https://www.w3.org/TR/json-ld11/#expanded-document-form): The expanded form provides a consistent representation of JSON-LD data by removing context information and expanding all terms to their full IRIs. All values are expressed as node objects or value objects with explicit `@id`, `@type`, `@value`, etc. The expanded form is useful for processing JSON-LD data in a consistent way, regardless of how it was originally formatted.

- [Compacted Document Form](https://www.w3.org/TR/json-ld11/#compacted-document-form): The compacted form is the most human-readable form of JSON-LD, using terms and compact IRIs instead of full IRIs. It applies a context to simplify the structure, representing string values directly as strings where possible, and using the most concise representation for lists, sets, and other data structures. Compaction makes JSON-LD documents more readable and easier to work with for developers.

- [Flattened Document Form](https://www.w3.org/TR/json-ld11/#flattened-document-form): The flattened form moves all node objects to the top level of the document, replacing embedded nodes with references. This form is useful for applications that need to access nodes directly by their identifier without traversing a nested structure. Flattening simplifies certain types of processing and can make it easier to perform operations on specific nodes.

- [Framed Document Form](https://www.w3.org/TR/json-ld11/#framed-document-form): The framed form allows restructuring a JSON-LD document according to a specified frame. Framing provides control over which nodes are represented as top-level objects and how nodes are embedded within each other. It's useful for reshaping JSON-LD data to match specific application requirements or to provide a more intuitive structure for specific use cases.

## APIs and Algorithms

- [JSON-LD Processing API](https://www.w3.org/TR/json-ld11-api/): The JSON-LD Processing API defines a set of functions for working with JSON-LD data, including:
  - `compact()`: Compacts a document according to a context
  - `expand()`: Expands a document, removing its context
  - `flatten()`: Flattens a document to a normalized form
  - `frame()`: Transforms a document according to a frame
  - `normalize()`: Normalizes a document using the RDF Dataset Normalization Algorithm
  - `toRdf()`: Converts JSON-LD to RDF
  - `fromRdf()`: Converts RDF to JSON-LD

- [Compaction Algorithm](https://www.w3.org/TR/json-ld11-api/#compaction): The compaction algorithm takes a JSON-LD document and a context, and produces a compacted document by applying the context to the document. It shortens IRIs to terms, simplifies values to their most concise representation, and organizes the document according to the context.

- [Expansion Algorithm](https://www.w3.org/TR/json-ld11-api/#expansion): The expansion algorithm takes a JSON-LD document and produces an expanded document by removing the context and expanding all terms to their full IRIs. It also converts values to their explicit representation as node objects or value objects.

- [Flattening Algorithm](https://www.w3.org/TR/json-ld11-api/#flattening): The flattening algorithm takes a JSON-LD document and produces a flattened document by moving all node objects to the top level and replacing embedded nodes with references. It can also apply compaction if a context is provided.

- [Framing Algorithm](https://www.w3.org/TR/json-ld11-framing/#framing-algorithm): The framing algorithm takes a JSON-LD document and a frame, and produces a framed document by restructuring the document according to the frame. The frame specifies which nodes should be top-level objects and how nodes should be embedded within each other.

- [RDF Serialization/Deserialization](https://www.w3.org/TR/json-ld11-api/#serialization-deserialization-algorithms): These algorithms convert between JSON-LD and RDF, allowing JSON-LD to be used as an RDF serialization format. The serialization algorithm converts RDF to JSON-LD, and the deserialization algorithm converts JSON-LD to RDF.

## Implementation Details

- [Python: PyLD Library](https://pyld.readthedocs.io/en/latest/): PyLD is a JSON-LD processor written in Python. It supports all features of JSON-LD 1.1, including compaction, expansion, flattening, framing, and RDF conversion. PyLD can be used to process JSON-LD documents in Python applications, with support for custom document loaders and other advanced features.

- [JavaScript: jsonld.js](https://github.com/digitalbazaar/jsonld.js): jsonld.js is a JSON-LD processor written in JavaScript. It provides a complete implementation of JSON-LD 1.1 for use in Node.js and browser environments. It supports all JSON-LD operations and includes utilities for working with JSON-LD in JavaScript applications.

- [Java: jsonld-java](https://github.com/jsonld-java/jsonld-java): jsonld-java is a JSON-LD processor for Java. It provides a Java API for working with JSON-LD documents and supports all JSON-LD operations. It can be integrated with popular Java frameworks and libraries for web development and data processing.

- [Framework Integration Examples](https://json-ld.org/learn.html): Examples of integrating JSON-LD with popular frameworks and platforms such as React, Angular, Django, Spring, and others.

## JSON-LD in Practice

- [Schema.org with JSON-LD](https://schema.org/docs/gs.html): Schema.org provides vocabularies for structured data on the internet, and JSON-LD is one of the recommended serialization formats. This resource explains how to use Schema.org vocabularies with JSON-LD for search engine optimization and rich snippets.

- [Web of Things (WoT) with JSON-LD](https://www.w3.org/TR/wot-thing-description/): The W3C Web of Things Thing Description uses JSON-LD as its data model. This resource explains how JSON-LD is used in the Web of Things ecosystem for describing devices and their capabilities.

- [Verifiable Credentials in JSON-LD](https://www.w3.org/TR/vc-data-model/): The Verifiable Credentials Data Model uses JSON-LD for expressing credentials in a way that is cryptographically secure, privacy-respecting, and machine-verifiable. This resource explains how JSON-LD is used in the Verifiable Credentials ecosystem.

- [JSON-LD Playground](https://json-ld.org/playground/): An interactive tool for experimenting with JSON-LD. It provides a way to try out JSON-LD compaction, expansion, flattening, and framing operations on sample documents or custom input.

## JSON-LD Structures vs RDF

- [Value Ordering](https://www.w3.org/TR/json-ld11/#value-ordering): JSON arrays imply order, but RDF graphs don't preserve order for properties with multiple values. JSON-LD bridges this gap by providing explicit mechanisms for representing both ordered and unordered collections:
  
  - **Arrays as Unordered Sets**: By default, arrays in JSON-LD represent unordered sets of values. When converted to RDF, each value becomes a separate triple with the same predicate, and the original order is not preserved.
  
  - **@list for Ordered Collections**: The `@list` keyword provides explicit ordering, representing an RDF List structure (linked nodes using `rdf:first`, `rdf:rest`, and `rdf:nil`). Lists can be defined either directly with the `@list` keyword or by setting `"@container": "@list"` in a term definition.
    ```json
    {
      "@context": {"foaf": "http://xmlns.com/foaf/0.1/"},
      "@id": "http://example.org/people#joebob",
      "foaf:nick": {"@list": ["joe", "bob", "jaybee"]}
    }
    ```
  
  - **@set for Explicit Unordered Collections**: The `@set` keyword explicitly marks a collection as unordered. While `@set` is often just syntactic sugar in the document body, it's useful in contexts to ensure values are always represented as arrays, even when there's only a single value.
    ```json
    {
      "@context": {
        "nick": {
          "@id": "http://xmlns.com/foaf/0.1/nick",
          "@container": "@set"
        }
      },
      "nick": ["joe", "bob"]
    }
    ```
  
  - **Combining with @container**: Since JSON-LD 1.1, `@set` can be combined with other container specifications to enforce array representations, such as `"@container": ["@index", "@set"]` or `"@container": ["@language", "@set"]`.
  
  - **Lists of Lists**: JSON-LD 1.1 fully supports representing nested lists, where values within a list object may themselves be list objects, enabling representation of complex ordered structures.

- [JSON Literals](https://www.w3.org/TR/json-ld11/#json-literals): JSON-LD supports preserving native JSON objects and arrays as literal values, which RDF traditionally couldn't represent directly. Using `"@type": "@json"` allows JSON-LD to preserve complex JSON structures that would otherwise be interpreted as nodes and properties.
  ```json
  {
    "@context": {
      "@version": 1.1,
      "e": {"@id": "http://example.com/vocab/json", "@type": "@json"}
    },
    "e": [56.0, {"d": true, "10": null, "1": []}]
  }
  ```

- [Index Maps](https://www.w3.org/TR/json-ld11/#index-maps): JSON-LD provides mechanisms for indexing values by various attributes, which have no direct equivalent in RDF. These include indexing by arbitrary keys, languages, node identifiers, and types.
  ```json
  {
    "@context": {
      "schema": "http://schema.org/",
      "name": "schema:name",
      "athletes": {
        "@id": "schema:athlete",
        "@container": "@index"
      }
    },
    "name": "San Francisco Giants",
    "athletes": {
      "catcher": {
        "@type": "schema:Person",
        "name": "Buster Posey"
      },
      "pitcher": {
        "@type": "schema:Person",
        "name": "Madison Bumgarner"
      }
    }
  }
  ```

## Optional

- [Relationship to RDF](https://www.w3.org/TR/json-ld11/#relationship-to-rdf): JSON-LD is a concrete RDF syntax, which means that a JSON-LD document is both an RDF document and a JSON document. This section explains the mapping between JSON-LD and RDF, including how JSON-LD's features map to RDF concepts like literals, blank nodes, and named graphs. It also covers the `rdf:JSON` datatype for representing JSON values in RDF and mechanisms for representing language and direction in RDF literals.

- [Embedding JSON-LD in HTML](https://www.w3.org/TR/json-ld11/#embedding-json-ld-in-html-documents): JSON-LD content can be embedded in HTML documents using the `<script>` element with `type="application/ld+json"`. This section explains how to embed JSON-LD in HTML, how the base IRI is determined, and how to handle character encoding issues. It also describes how to reference specific JSON-LD script elements within an HTML document.

- [Security Considerations](https://www.w3.org/TR/json-ld11/#security-considerations): This section discusses security considerations when working with JSON-LD, including the risks of loading remote contexts, the potential for resource exhaustion attacks, and the need to sanitize input. It provides guidance on how to mitigate these risks, such as caching remote contexts and restricting which contexts are allowed to be loaded.

- [Privacy Considerations](https://www.w3.org/TR/json-ld11/#privacy-considerations): This section discusses privacy considerations when working with JSON-LD, including the potential for revealing information through the retrieval of remote contexts and the possibility of fingerprinting based on context usage patterns. It provides guidance on how to address these concerns, such as using local copies of contexts and being mindful of which contexts are included in documents.

- [Internationalization Considerations](https://www.w3.org/TR/json-ld11/#internationalization-considerations): This section discusses internationalization considerations when working with JSON-LD, including support for language-tagged strings and base direction indicators. It explains the limitations of the current RDF data model for representing text direction and provides guidance on how to handle internationalization issues in JSON-LD documents.

- [Media Type Definition](https://www.w3.org/TR/json-ld11/#iana-considerations): The media type for JSON-LD is `application/ld+json`. This section provides the formal media type definition, including parameters, encoding considerations, security considerations, and interoperability considerations. It also defines fragment identifier behavior and explains how to use the `profile` parameter to request specific JSON-LD document forms.

- [Changes Since JSON-LD 1.0](https://www.w3.org/TR/json-ld11/#changes-since-1-0-recommendation-of-16-january-2014): This section summarizes the changes made in JSON-LD 1.1 compared to JSON-LD 1.0. It lists new features, modified behaviors, and other changes that might affect compatibility between the two versions. This information is useful for developers transitioning from JSON-LD 1.0 to JSON-LD 1.1 and for understanding which features are new in the 1.1 specification.
