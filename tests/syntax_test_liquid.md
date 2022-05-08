| SYNTAX TEST "Packages/Liquid/Syntaxes/Markdown (Liquid).sublime-syntax"

# Header #{{20}} #
| ^^^^^^^^^^^^^^ markup.heading.1.markdown entity.name.section.markdown
|         ^^^^^^ meta.object.liquid
|         ^^ punctuation.definition.object.begin.liquid
|           ^^ constant.numeric.value.liquid
|             ^^ punctuation.definition.object.end.liquid

<style>
    hr {
        {% if true %}
|       ^^^^^^^^^^^^^ meta.disable-markdown source.css.embedded.html meta.property-list.css meta.block.css meta.tag.liquid
|       ^^ punctuation.definition.tag.begin.liquid
|          ^^ keyword.control.conditional.liquid
|             ^^^^ constant.language.boolean.liquid
|                  ^^ punctuation.definition.tag.end.liquid
        font-{{family}}: "{{font}}";
|            ^^^^^^^^^^ meta.disable-markdown source.css.embedded.html meta.property-list.css meta.block.css meta.object.liquid
|            ^^ punctuation.definition.object.begin.liquid
|              ^^^^^^ variable.other.liquid
|                    ^^ punctuation.definition.object.end.liquid
|                        ^ meta.string.css string.quoted.double.css punctuation.definition.string.begin.css
|                         ^^^^^^^^ meta.disable-markdown source.css.embedded.html meta.property-list.css meta.block.css meta.property-value.css meta.string.css meta.interpolation.liquid meta.object.liquid
|                         ^^ punctuation.definition.object.begin.liquid
|                           ^^^^ variable.other.liquid
|                               ^^ punctuation.definition.object.end.liquid
|                                 ^ meta.string.css string.quoted.double.css punctuation.definition.string.end.css
        {% endif %}
|       ^^^^^^^^^^^ meta.disable-markdown source.css.embedded.html meta.property-list.css meta.block.css meta.tag.liquid
|       ^^ punctuation.definition.tag.begin.liquid
|          ^^^^^ keyword.control.conditional.liquid
|                ^^ punctuation.definition.tag.end.liquid
    }
</style>

<script>
    function foo({{args_list}}) {
|                ^^^^^^^^^^^^^ meta.disable-markdown source.js.embedded.html meta.function.parameters.js meta.object.liquid
        {% for i in vars %}
|       ^^^^^^^^^^^^^^^^^^^ meta.disable-markdown source.js.embedded.html meta.function.js meta.block.js meta.tag.liquid
        {% endfor %}
|       ^^^^^^^^^^^^ meta.disable-markdown source.js.embedded.html meta.function.js meta.block.js meta.tag.liquid
    }
|   ^ meta.disable-markdown source.js.embedded.html meta.function.js meta.block.js punctuation.section.block.end.js
</script>

<div attrib="{{obj}}">
|            ^^^^^^^ meta.disable-markdown meta.tag.block.any.html meta.attribute-with-value.html meta.string.html meta.interpolation.liquid meta.object.liquid
    {% if true %}
|   ^^^^^^^^^^^^^ meta.disable-markdown meta.tag.liquid
    A Paragraph {{var}}
|               ^^^^^^^ meta.disable-markdown meta.object.liquid
    {% endif %}
|   ^^^^^^^^^^^ meta.disable-markdown meta.tag.liquid
</div>
|^^^^^ meta.disable-markdown meta.tag.block.any.html


{% if true %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^ keyword.control.conditional.liquid
|     ^^^^ constant.language.boolean.liquid
|          ^^ punctuation.definition.tag.end.liquid

A Paragraph {{var}}
|           ^^^^^^^ meta.paragraph.markdown meta.object.liquid
{% endif %}
| <- meta.paragraph.markdown meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^ meta.paragraph.markdown meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^^ keyword.control.conditional.liquid
|        ^^ punctuation.definition.tag.end.liquid
