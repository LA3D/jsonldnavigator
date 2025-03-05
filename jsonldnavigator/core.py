"""jsonldnavigator"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../00_core.ipynb.

# %% auto 0
__all__ = ['JsonLdNavigator', 'create_schema_index', 'get_class_details', 'get_property_details', 'get_class_properties',
           'find_related_classes', 'search_terms', 'get_property_path', 'L', 'safe_text']

# %% ../00_core.ipynb 4
from fastcore.foundation import patch  # @patch
from httpx import get as xget, post as xpost
from bs4 import BeautifulSoup as bs
from fastcore.utils import *
import json
from typing import Any, Dict, List, Optional, Union
from pyld import jsonld  # For JSON-LD processing
from claudette import *

# %% ../00_core.ipynb 5
class JsonLdNavigator:
    "Navigator for JSON-LD documents with semantic understanding"
    def __init__(self, jsonld_data):
        "Initialize with JSON-LD data"
        self.data = jsonld_data if not isinstance(jsonld_data, str) else json.loads(jsonld_data)
        self.index = create_schema_index(self.data)
        
    def get_class(self, class_id):
        "Get details about a class"
        return get_class_details(self.data, class_id)
    
    def get_property(self, property_id):
        "Get details about a property"
        return get_property_details(self.data, property_id)
    
    def get_properties_for(self, class_id, include_inherited=True):
        "Get properties applicable to a class"
        return get_class_properties(self.data, class_id, include_inherited)
    
    def find_related(self, class_id):
        "Find classes related to the specified class"
        return find_related_classes(self.data, class_id)
    
    def search(self, query):
        "Search for classes or properties matching query"
        return search_terms(self.data, query)
    
    def find_path(self, source_class, target_class, max_depth=2):
        "Find property paths between classes"
        return get_property_path(self.data, source_class, target_class, max_depth)
    
    def show_index(self):
        "Show a summary of the index"
        vocab = self.index["vocabularies"]["schema.org"]
        print(f"Schema.org Index:")
        print(f"- Classes: {vocab['class_count']}")
        print(f"- Properties: {vocab['property_count']}")
        print(f"\nAvailable Affordances:")
        for name, desc in self.index["affordances"].items():
            print(f"- {name}: {desc}")
        
    def __repr__(self):
        vocab = self.index["vocabularies"]["schema.org"]
        return f"JsonLdNavigator(classes={vocab['class_count']}, properties={vocab['property_count']})"

# %% ../00_core.ipynb 6
class JsonLdNavigator:
    "Navigator for JSON-LD documents with semantic understanding"
    def __init__(self, jsonld_data):
        "Initialize with JSON-LD data"
        self.data = jsonld_data if not isinstance(jsonld_data, str) else json.loads(jsonld_data)
        self.index = create_schema_index(self.data)
        
    def get_class(self, class_id):
        "Get details about a class"
        return get_class_details(self.data, class_id)
    
    def get_property(self, property_id):
        "Get details about a property"
        return get_property_details(self.data, property_id)
    
    def get_properties_for(self, class_id, include_inherited=True):
        "Get properties applicable to a class"
        return get_class_properties(self.data, class_id, include_inherited)
    
    def find_related(self, class_id):
        "Find classes related to the specified class"
        return find_related_classes(self.data, class_id)
    
    def search(self, query):
        "Search for classes or properties matching query"
        return search_terms(self.data, query)
    
    def find_path(self, source_class, target_class, max_depth=2):
        "Find property paths between classes"
        return get_property_path(self.data, source_class, target_class, max_depth)
    
    def show_index(self):
        "Show a summary of the index"
        vocab = self.index["vocabularies"]["schema.org"]
        print(f"Schema.org Index:")
        print(f"- Classes: {vocab['class_count']}")
        print(f"- Properties: {vocab['property_count']}")
        print(f"\nAvailable Affordances:")
        for name, desc in self.index["affordances"].items():
            print(f"- {name}: {desc}")
        
    def __repr__(self):
        vocab = self.index["vocabularies"]["schema.org"]
        return f"JsonLdNavigator(classes={vocab['class_count']}, properties={vocab['property_count']})"

# %% ../00_core.ipynb 7
# Core indexing function
def create_schema_index(jsonld_data):
    "Create a semantic index from JSON-LD data"
    index = {
        "vocabularies": {
            "schema.org": {
                "prefix": "schema",
                "namespace": "https://schema.org/",
                "description": "Schema.org vocabulary for structured data",
                "classes": [],
                "properties": [],
                "class_count": 0,
                "property_count": 0
            }
        },
        "class_hierarchy": {},  # Tree structure of classes
        "property_groups": {},  # Properties grouped by domain/function
        "affordances": {
            "get_class(class_id)": "Get detailed information about a class",
            "get_property(property_id)": "Get detailed information about a property",
            "get_properties_for(class_id, include_inherited=True)": "Get properties for a class",
            "find_related(class_id)": "Find classes semantically related to this class",
            "search(query)": "Search for classes or properties matching a query",
            "find_path(source_class, target_class)": "Find property paths between classes"
        }
    }
    
    # Process classes and build class hierarchy
    class_hierarchy = {}
    for item in jsonld_data.get('@graph', []):
        if item.get('@type') == 'rdfs:Class':
            class_id = item.get('@id')
            class_name = safe_text(item.get('rdfs:label'))
            
            if class_name:
                index["vocabularies"]["schema.org"]["classes"].append(class_name)
                index["vocabularies"]["schema.org"]["class_count"] += 1
                
                # Add to class hierarchy
                parent_class = item.get('rdfs:subClassOf', {}).get('@id')
                if parent_class:
                    if parent_class not in class_hierarchy:
                        class_hierarchy[parent_class] = []
                    class_hierarchy[parent_class].append(class_id)
    
    index["class_hierarchy"] = class_hierarchy
    
    # Process properties and group them
    property_groups = {
        "identification": [],  # Properties for identifying things
        "descriptive": [],     # Properties for describing things
        "relational": [],      # Properties linking to other entities
        "temporal": [],        # Time-related properties
        "other": []            # Other properties
    }
    
    for item in jsonld_data.get('@graph', []):
        if item.get('@type') == 'rdf:Property':
            prop_id = item.get('@id')
            prop_name = safe_text(item.get('rdfs:label'))
            
            if prop_name:
                index["vocabularies"]["schema.org"]["properties"].append(prop_name)
                index["vocabularies"]["schema.org"]["property_count"] += 1
                
                # Simple property categorization
                if prop_name in ['identifier', 'url', 'name', 'id']:
                    property_groups["identification"].append(prop_id)
                elif prop_name in ['description', 'text', 'keywords']:
                    property_groups["descriptive"].append(prop_id)
                elif any(x in prop_name.lower() for x in ['date', 'time', 'duration']):
                    property_groups["temporal"].append(prop_id)
                else:
                    # Check if it links to another entity by examining ranges
                    ranges = item.get('schema:rangeIncludes', [])
                    if not isinstance(ranges, list): ranges = [ranges]
                    
                    if any('schema:' in r.get('@id', '') for r in ranges if r):
                        property_groups["relational"].append(prop_id)
                    else:
                        property_groups["other"].append(prop_id)
    
    index["property_groups"] = property_groups
    
    return index


# %% ../00_core.ipynb 8
# Core navigation functions
def get_class_details(jsonld_data, class_id):
    "Get detailed information about a specific class"
    for item in jsonld_data.get('@graph', []):
        if item.get('@id') == class_id:
            return {
                "id": item.get('@id'),
                "label": item.get('rdfs:label'),
                "description": item.get('rdfs:comment'),
                "parent_class": item.get('rdfs:subClassOf', {}).get('@id'),
                "equivalent_classes": [c.get('@id') for c in L(item.get('owl:equivalentClass'))]
            }
    return {"error": f"Class {class_id} not found"}

# %% ../00_core.ipynb 9
def get_property_details(jsonld_data, property_id):
    "Get detailed information about a specific property"
    for item in jsonld_data.get('@graph', []):
        if item.get('@id') == property_id:
            # Handle domains and ranges which might be lists or single items
            domains = item.get('schema:domainIncludes', [])
            if not isinstance(domains, list): domains = [domains]
            domain_ids = [d.get('@id') for d in domains if d]
            
            ranges = item.get('schema:rangeIncludes', [])
            if not isinstance(ranges, list): ranges = [ranges]
            range_ids = [r.get('@id') for r in ranges if r]
            
            return {
                "id": item.get('@id'),
                "label": item.get('rdfs:label'),
                "description": item.get('rdfs:comment'),
                "domains": domain_ids,
                "ranges": range_ids,
                "subproperty_of": item.get('rdfs:subPropertyOf', {}).get('@id')
            }
    return {"error": f"Property {property_id} not found"}


# %% ../00_core.ipynb 10
def get_class_properties(jsonld_data, class_id, include_inherited=True):
    "Get properties applicable to a class"
    properties = []
    
    # Get class hierarchy if including inherited properties
    class_hierarchy = [class_id]
    if include_inherited:
        current_class = get_class_details(jsonld_data, class_id)
        while current_class and 'error' not in current_class:
            parent_class = current_class.get('parent_class')
            if parent_class and parent_class not in class_hierarchy:
                class_hierarchy.append(parent_class)
                current_class = get_class_details(jsonld_data, parent_class)
            else:
                break
    
    # Find properties for each class in the hierarchy
    for item in jsonld_data.get('@graph', []):
        if item.get('@type') == 'rdf:Property':
            domains = item.get('schema:domainIncludes', [])
            if not isinstance(domains, list): domains = [domains]
            domain_ids = [d.get('@id') for d in domains if d]
            
            # Check if any class in the hierarchy is in the domains
            if any(cls_id in domain_ids for cls_id in class_hierarchy):
                prop = {
                    "id": item.get('@id'),
                    "label": item.get('rdfs:label'),
                    "description": item.get('rdfs:comment')[:100] + "..." 
                        if item.get('rdfs:comment') and len(item.get('rdfs:comment')) > 100 
                        else item.get('rdfs:comment'),
                    "inherited": class_id != domain_ids[0] if domain_ids else False
                }
                properties.append(prop)
    
    return properties



# %% ../00_core.ipynb 11
def find_related_classes(jsonld_data, class_id):
    """Find classes related to the specified class through properties"""
    related = {
        "parent_classes": [],
        "child_classes": [],
        "referenced_by": [],
        "references": []
    }
    
    # Find parent class
    for item in jsonld_data.get('@graph', []):
        if item.get('@id') == class_id and item.get('@type') == 'rdfs:Class':
            parent = item.get('rdfs:subClassOf', {}).get('@id')
            if parent:
                related["parent_classes"].append(parent)
    
    # Find child classes
    for item in jsonld_data.get('@graph', []):
        if item.get('@type') == 'rdfs:Class':
            parent = item.get('rdfs:subClassOf', {}).get('@id')
            if parent == class_id:
                related["child_classes"].append(item.get('@id'))
    
    # Find classes referenced by this class's properties
    properties = get_class_properties(jsonld_data, class_id)
    for prop in properties:
        prop_details = get_property_details(jsonld_data, prop.get('id'))
        for range_class in prop_details.get('ranges', []):
            if range_class not in related["references"]:
                related["references"].append(range_class)
    
    # Find classes that reference this class
    for item in jsonld_data.get('@graph', []):
        if item.get('@type') == 'rdf:Property':
            domains = item.get('schema:domainIncludes', [])
            if not isinstance(domains, list): domains = [domains]
            domain_ids = [d.get('@id') for d in domains if d]
            
            ranges = item.get('schema:rangeIncludes', [])
            if not isinstance(ranges, list): ranges = [ranges]
            range_ids = [r.get('@id') for r in ranges if r]
            
            if class_id in range_ids:
                for domain in domain_ids:
                    if domain not in related["referenced_by"]:
                        related["referenced_by"].append(domain)
    
    return related


# %% ../00_core.ipynb 12
def search_terms(jsonld_data, query):
    """Search for classes or properties matching a query string"""
    results = {
        "classes": [],
        "properties": []
    }
    
    query = query.lower()
    
    for item in jsonld_data.get('@graph', []):
        label = str(item.get('rdfs:label', '')).lower()
        description = str(item.get('rdfs:comment', '')).lower()
        
        if query in label or query in description:
            result = {
                "id": item.get('@id'),
                "label": item.get('rdfs:label'),
                "description": item.get('rdfs:comment')[:100] + "..." 
                    if item.get('rdfs:comment') and len(item.get('rdfs:comment')) > 100 
                    else item.get('rdfs:comment')
            }
            
            if item.get('@type') == 'rdfs:Class':
                results["classes"].append(result)
            elif item.get('@type') == 'rdf:Property':
                results["properties"].append(result)
    
    return results



# %% ../00_core.ipynb 13
def get_property_path(jsonld_data, source_class, target_class, max_depth=2):
    """Find property paths between two classes"""
    paths = []
    
    # Get properties of the source class
    properties = get_class_properties(jsonld_data, source_class)
    
    # First level - direct connections
    for prop in properties:
        prop_details = get_property_details(jsonld_data, prop.get('id'))
        if target_class in prop_details.get('ranges', []):
            paths.append({
                "path": [{"class": source_class, "property": prop.get('id'), "target": target_class}],
                "description": f"{source_class} → {prop.get('label')} → {target_class}"
            })
    
    # Second level - if max_depth > 1
    if max_depth > 1 and not paths:
        for prop in properties:
            prop_details = get_property_details(jsonld_data, prop.get('id'))
            for intermediate_class in prop_details.get('ranges', []):
                # Skip if not a class (like literal values)
                if not intermediate_class.startswith('schema:'):
                    continue
                    
                # Check if this intermediate class has properties to the target
                intermediate_properties = get_class_properties(jsonld_data, intermediate_class)
                for int_prop in intermediate_properties:
                    int_prop_details = get_property_details(jsonld_data, int_prop.get('id'))
                    if target_class in int_prop_details.get('ranges', []):
                        paths.append({
                            "path": [
                                {"class": source_class, "property": prop.get('id'), "target": intermediate_class},
                                {"class": intermediate_class, "property": int_prop.get('id'), "target": target_class}
                            ],
                            "description": f"{source_class} → {prop.get('label')} → {intermediate_class} → {int_prop.get('label')} → {target_class}"
                        })
    
    return paths




# %% ../00_core.ipynb 15
# Helper function to always return a list
def L(x): return x if isinstance(x, list) else [x] if x is not None else []


# %% ../00_core.ipynb 16
def safe_text(value):
    "Safely extract text from a JSON-LD value which might be a string or a dict"
    if value is None:
        return ""
    if isinstance(value, dict):
        return str(value.get('@value', ''))
    return str(value)
