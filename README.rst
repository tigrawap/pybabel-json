PyBabel-JSON
===============

Release notes
--------------
- 0.2.0 - Added Python 3 support.
- 0.1.0 - Initial release.

Installation
--------------
pip install pybabel-json

Usage
-------
Add `[json: path/\*\*.json]` to babel.cfg

Dependencies
------------------

- Uses javascript lexer built in into babel, so no dependencies but babel itself

Key features:
--------------------------------
- Two JSON formats supported: plain string and custom gettext_string format
- Keys are usually ignored, the only exception are objects with "type":"gettext_string"
- Keys are mainly used for logical separation of lists of values that should be translated
- Lists also supported, both in plain strings and gettext_string format

.. code-block:: json

    {
        "simple_format_with_tree":{
            "inner":{
                "tree":{
                    "key1":"Some key to translate",
                    "key2":"Another key to translate",
                    "key3":"Repeating key to translate",
                    "key4":"Repeating key to translate"
                }
            }
        },
        "gettext_format_key1":{
            "type":"gettext_string",
            "funcname":"ngettext",
            "content":"Singular string",
            "alt_content":"Plural string"
        },
        "gettext_format_key2":{
            "type":"gettext_string",
            "funcname":"ngettext",
            "content":"Another singular string",
            "alt_content":"Another plural string"
        },
        "list_of_values":[
            "one",
            "two",
            "three"
        ],
        "list_of_gettexts":[
            {
                "type" : "gettext_string",
                "funcname" : "ngettext",
                "content" : "list_string 1",
                "alt_content" : "plural list_string1"
            },
            {
                "type" : "gettext_string",
                "funcname" : "ngettext",
                "content" : "list_string 2",
                "alt_content" : "plural list_string2"
            }
        ]
    }
