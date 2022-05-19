| SYNTAX TEST "Packages/Liquid/Syntaxes/Markdown (Liquid).sublime-syntax"

<!--
 --- Test Liquid Control Flow
 --- https://shopify.github.io/liquid/tags/control-flow
 -->

{% if true %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^ keyword.control.conditional.if.liquid
|     ^^^^ constant.language.boolean.liquid
|          ^^ punctuation.definition.tag.end.liquid

A Paragraph {{var}}
|           ^^^^^^^ meta.object.liquid

{% elsif foo %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^^ keyword.control.conditional.elseif.liquid
|        ^^^ variable.other.liquid
|            ^^ punctuation.definition.tag.end.liquid

{% else %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^ keyword.control.conditional.else.liquid
|       ^^ punctuation.definition.tag.end.liquid

{% endif %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^^ keyword.control.conditional.end.liquid
|        ^^ punctuation.definition.tag.end.liquid

{% if product.tags contains "Hello" %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^ keyword.control.conditional.if.liquid
|     ^^^^^^^ variable.other.liquid
|            ^ punctuation.accessor.dot.liquid
|             ^^^^ variable.other.member.liquid
|                  ^^^^^^^^ keyword.operator.logical.liquid
|                           ^^^^^^^ meta.string.liquid string.quoted.double.liquid
|                                   ^^ punctuation.definition.tag.end.liquid

{% case handle %}
|^^^^^^^^^^^^^^^^ meta.tag.liquid
|  ^^^^ keyword.control.conditional.case.liquid
|       ^^^^^^ variable.other.liquid
  {% when "cake" %}
| ^^^^^^^^^^^^^^^^^ meta.tag.liquid
|    ^^^^ keyword.control.conditional.when.liquid
|         ^^^^^^ meta.string.liquid string.quoted.double.liquid
     This is a cake
  {% when "cookie", "biscuit" %}
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|    ^^^^ keyword.control.conditional.when.liquid
|         ^^^^^^^^ meta.string.liquid string.quoted.double.liquid
|                 ^ punctuation.separator.sequence.liquid
|                   ^^^^^^^^^ meta.string.liquid string.quoted.double.liquid
     This is a cookie
  {% else %}
| ^^^^^^^^^^ meta.tag.liquid
|    ^^^^ keyword.control.conditional.else.liquid
     This is not a cake nor a cookie
{% endcase %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^ meta.tag.liquid
|  ^^^^^^^ keyword.control.conditional.end.liquid

{% liquid
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^^^ entity.name.tag.liquid

case section.blocks.size
| <- meta.tag.liquid keyword.control.conditional.case.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid

when 1
| <- meta.tag.liquid keyword.control.conditional.when.liquid
|^^^^^^ meta.tag.liquid
|^^^ keyword.control.conditional.when.liquid
|    ^ constant.numeric.value.liquid

  assign column_size = ''
|^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
| ^^^^^^ keyword.control.liquid
|        ^^^^^^^^^^^ variable.other.liquid
|                    ^ keyword.operator.assignment.liquid
|                      ^^ meta.string.liquid string.quoted.single.liquid

when 2
| <- meta.tag.liquid keyword.control.conditional.when.liquid

  assign column_size = 'one-half'
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
| ^^^^^^ keyword.control.liquid
|        ^^^^^^^^^^^ variable.other.liquid
|                    ^ keyword.operator.assignment.liquid
|                      ^^^^^^^^^^ meta.string.liquid string.quoted.single.liquid

else
| <- meta.tag.liquid keyword.control.conditional.else.liquid

  assign column_size = 'one-quarter'
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
| ^^^^^^ keyword.control.liquid
|        ^^^^^^^^^^^ variable.other.liquid
|                    ^ keyword.operator.assignment.liquid
|                      ^^^^^^^^^^^^^ meta.string.liquid string.quoted.single.liquid

endcase %}
| <- meta.tag.liquid keyword.control.conditional.end.liquid
|^^^^^^^^^ meta.tag.liquid
|^^^^^^ keyword.control.conditional.end.liquid
|       ^^ punctuation.definition.tag.end.liquid


<!--
 --- Test Iteration Statements
 --- https://shopify.github.io/liquid/tags/iteration/
-->

{% for %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^ meta.tag.liquid
|  ^^^ keyword.control.loop.for.liquid

{% for item in array limit:2 %}
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|                    ^^^^^ variable.parameter.loop.liquid
|                         ^ punctuation.separator.key-value.liquid
|                          ^ constant.numeric.value.liquid

{% for item in array offset:2 %}
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|                    ^^^^^^ variable.parameter.loop.liquid
|                          ^ punctuation.separator.key-value.liquid
|                           ^ constant.numeric.value.liquid

{% for item in array reversed %}
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|                    ^^^^^^^^ variable.parameter.loop.liquid

{% for i in (1..5) %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|  ^^^ keyword.control.loop.for.liquid
|      ^ variable.other.liquid
|        ^^ keyword.operator.logical.liquid
|           ^^^^^^ meta.sequence.range.liquid
|           ^ punctuation.section.sequence.begin.liquid
|            ^ constant.numeric.value.liquid
|             ^^ punctuation.separator.range.liquid
|               ^ constant.numeric.value.liquid
|                ^ punctuation.section.sequence.end.liquid
|                  ^^ punctuation.definition.tag.end.liquid

{% for i in (1..num) %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|  ^^^ keyword.control.loop.for.liquid
|      ^ variable.other.liquid
|        ^^ keyword.operator.logical.liquid
|           ^^^^^^^^ meta.sequence.range.liquid
|           ^ punctuation.section.sequence.begin.liquid
|            ^ constant.numeric.value.liquid
|             ^^ punctuation.separator.range.liquid
|               ^^^ variable.other.liquid
|                  ^ punctuation.section.sequence.end.liquid
|                    ^^ punctuation.definition.tag.end.liquid

{% for product in collection.products %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^ keyword.control.loop.for.liquid
|      ^^^^^^^ variable.other.liquid
|              ^^ keyword.operator.logical.liquid
|                 ^^^^^^^^^^ variable.other.liquid
|                           ^ punctuation.accessor.dot.liquid
|                            ^^^^^^^^ variable.other.member.liquid
|                                     ^^ punctuation.definition.tag.end.liquid

  {% cycle "one", "two", "three" %}
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
| ^^ punctuation.definition.tag.begin.liquid
|    ^^^^^ support.function.cycle.liquid
|          ^^^^^ meta.string.liquid string.quoted.double.liquid
|               ^ punctuation.separator.sequence.liquid
|                 ^^^^^ meta.string.liquid string.quoted.double.liquid
|                      ^ punctuation.separator.sequence.liquid
|                        ^^^^^^^ meta.string.liquid string.quoted.double.liquid
|                                ^^ punctuation.definition.tag.end.liquid

  {% cycle "first": "one", "two", "three" %}
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
| ^^ punctuation.definition.tag.begin.liquid
|    ^^^^^ support.function.cycle.liquid
|          ^^^^^^^ constant.other.group.liquid
|          ^ punctuation.definition.constant.begin.liquid
|                ^ punctuation.definition.constant.end.liquid
|                 ^ punctuation.separator.key-value.liquid
|                   ^^^^^ meta.string.liquid string.quoted.double.liquid
|                        ^ punctuation.separator.sequence.liquid

  {% cycle 'first': 'one', 'two', 'three' %}
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
| ^^ punctuation.definition.tag.begin.liquid
|    ^^^^^ support.function.cycle.liquid
|          ^^^^^^^ constant.other.group.liquid
|          ^ punctuation.definition.constant.begin.liquid
|                ^ punctuation.definition.constant.end.liquid
|                 ^ punctuation.separator.key-value.liquid
|                   ^^^^^ meta.string.liquid string.quoted.single.liquid
|                        ^ punctuation.separator.sequence.liquid

  {% break %}
| ^^^^^^^^^^^ meta.tag.liquid
| ^^ punctuation.definition.tag.begin.liquid
|    ^^^^^ keyword.control.flow.break.liquid
|          ^^ punctuation.definition.tag.end.liquid

{% else %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^ keyword.control.conditional.else.liquid
|       ^^ punctuation.definition.tag.end.liquid

  {% continue %}
| ^^^^^^^^^^^^^^ meta.tag.liquid
| ^^ punctuation.definition.tag.begin.liquid
|    ^^^^^^^^ keyword.control.flow.continue.liquid
|             ^^ punctuation.definition.tag.end.liquid

{% endfor %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^^^ keyword.control.loop.end.liquid
|         ^^ punctuation.definition.tag.end.liquid

{% tablerow product in (1..collection.products) cols:4 limit:5 offset:1 %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^^^^^ keyword.control.loop.tablerow.liquid
|           ^^^^^^^ variable.other.liquid
|                   ^^ keyword.operator.logical.liquid
|                      ^^^^^^^^^^^^^^^^^^^^^^^^ meta.sequence.range.liquid
|                      ^ punctuation.section.sequence.begin.liquid
|                       ^ constant.numeric.value.liquid
|                        ^^ punctuation.separator.range.liquid
|                          ^^^^^^^^^^ variable.other.liquid
|                                    ^ punctuation.accessor.dot.liquid
|                                     ^^^^^^^^ variable.other.member.liquid
|                                             ^ punctuation.section.sequence.end.liquid
|                                               ^^^^ variable.parameter.loop.liquid
|                                                   ^ punctuation.separator.key-value.liquid
|                                                    ^ constant.numeric.value.liquid
|                                                      ^^^^^ variable.parameter.loop.liquid
|                                                           ^ punctuation.separator.key-value.liquid
|                                                            ^ constant.numeric.value.liquid
|                                                              ^^^^^^ variable.parameter.loop.liquid
|                                                                    ^ punctuation.separator.key-value.liquid
|                                                                     ^ constant.numeric.value.liquid
|                                                                       ^^ punctuation.definition.tag.end.liquid

{% endtablerow %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^^^^^^^^ keyword.control.loop.end.liquid
|              ^^ punctuation.definition.tag.end.liquid

{% liquid
for product in collection.products
| <- meta.tag.liquid keyword.control.loop.for.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|^^ keyword.control.loop.for.liquid
|   ^^^^^^^ variable.other.liquid
|           ^^ keyword.operator.logical.liquid
|              ^^^^^^^^^^ variable.other.liquid
|                        ^ punctuation.accessor.dot.liquid
|                         ^^^^^^^^ variable.other.member.liquid
  echo product.title | capitalize
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
| ^^^^ support.function.liquid
|      ^^^^^^^ variable.other.liquid
|             ^ punctuation.accessor.dot.liquid
|              ^^^^^ variable.other.member.liquid
|                    ^ keyword.operator.logical.pipe.liquid
|                      ^^^^^^^^^^ support.function.filter.liquid
endfor %}
| <- meta.tag.liquid keyword.control.loop.end.liquid
|^^^^^^^^ meta.tag.liquid
|^^^^^ keyword.control.loop.end.liquid
|      ^^ punctuation.definition.tag.end.liquid

<!--
 --- Variable Statements
 --- https://shopify.github.io/liquid/tags/variable
 -->

{% assign handle = "cake" %}
|^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|  ^^^^^^ keyword.control.liquid
|         ^^^^^^ variable.other.liquid
|                ^ keyword.operator.assignment.liquid
|                  ^^^^^^ meta.string.liquid string.quoted.double.liquid

{% assign foo = bar | where: "type", "baz" %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^^^ keyword.control.liquid
|         ^^^ variable.other.liquid
|             ^ keyword.operator.assignment.liquid
|               ^^^ variable.other.liquid
|                   ^ keyword.operator.logical.pipe.liquid
|                     ^^^^^ support.function.filter.liquid
|                          ^ punctuation.separator.key-value.liquid
|                            ^^^^^^ meta.string.liquid string.quoted.double.liquid
|                                  ^ punctuation.separator.sequence.liquid
|                                    ^^^^^ meta.string.liquid string.quoted.double.liquid
|                                          ^^ punctuation.definition.tag.end.liquid

{% capture about_me %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^^^^ keyword.control.liquid
|          ^^^^^^^^ variable.other.liquid
|                   ^^ punctuation.definition.tag.end.liquid

I am {{ age }} and my favorite food is {{ favorite_food }}.
|    ^^^^^^^^^ meta.object.liquid
|                                      ^^^^^^^^^^^^^^^^^^^ meta.object.liquid

{% endcapture %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^^^^^^^ keyword.control.liquid
|             ^^ punctuation.definition.tag.end.liquid

{% increment my_counter %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^^^^^^ support.function.liquid
|            ^^^^^^^^^^ variable.other.liquid
|                       ^^ punctuation.definition.tag.end.liquid

{% decrement my_counter %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^^^^^^ support.function.liquid
|            ^^^^^^^^^^ variable.other.liquid
|                       ^^ punctuation.definition.tag.end.liquid


<!--
 --- Template Tests
 --- https://shopify.github.io/liquid/tags/template
 -->

{% comment %}
| <- comment.block.liquid meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^ comment.block.liquid meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^^^^ keyword.declaration.comment.liquid
|          ^^ punctuation.definition.tag.end.liquid

{% assign verb = "converted" %}
| <- comment.block.liquid - meta.tag
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ comment.block.liquid - meta.tag

{% endcomment %}
| <- comment.block.liquid meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^^ comment.block.liquid meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^^^^^^^ keyword.declaration.comment.liquid
|             ^^ punctuation.definition.tag.end.liquid

{% javascript %}
| <- meta.tag.liquid punctuation.definition.tag.schema.begin.liquid
|^^^^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.schema.begin.liquid
|  ^^^^^^^^^^ keyword.declaration.raw.liquid
|             ^^ punctuation.definition.tag.schema.end.liquid
  function foo() { return 0; }
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ source.js.embedded.liquid
{% endjavascript %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^^^^^^^^^^ keyword.declaration.raw.liquid
|                ^^ punctuation.definition.tag.end.liquid

{% raw %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^ keyword.declaration.raw.liquid
|      ^^ punctuation.definition.tag.end.liquid

In Handlebars, {{ this }} will be HTML-escaped, but {{{ that }}} will not.
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.raw.liquid
|              ^^^^^^^^^^ - meta.object.liquid
|                                                   ^^^^^^^^^^^^ - meta.object.liquid

{% raw %}
|^^^^^^^^^ meta.raw.liquid - meta.tag - punctuation - keyword

{% endraw %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^^^ keyword.declaration.raw.liquid
|         ^^ punctuation.definition.tag.end.liquid

{% include "template-name" %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^^^^ keyword.control.import.liquid
|          ^^^^^^^^^^^^^^^ meta.string.liquid string.quoted.double.liquid
|                          ^^ punctuation.definition.tag.end.liquid

{% render "product", product: featured_product %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^^^ support.function.liquid
|         ^^^^^^^^^ meta.string.liquid string.quoted.double.liquid
|                  ^ punctuation.separator.sequence.liquid
|                    ^^^^^^^ variable.parameter.liquid
|                           ^ punctuation.separator.key-value.liquid
|                             ^^^^^^^^^^^^^^^^ variable.other.liquid
|                                              ^^ punctuation.definition.tag.end.liquid

{% render "product" with featured_product as product %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^^^ support.function.liquid
|         ^^^^^^^^^ meta.string.liquid string.quoted.double.liquid
|                   ^^^^ keyword.declaration.with.liquid
|                        ^^^^^^^^^^^^^^^^ variable.other.liquid
|                                         ^^ keyword.operator.assignment.liquid
|                                            ^^^^^^^ variable.other.liquid
|                                                    ^^ punctuation.definition.tag.end.liquid

{% render "product_variant" for variants as variant %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^^^ support.function.liquid
|         ^^^^^^^^^^^^^^^^^ meta.string.liquid string.quoted.double.liquid
|                           ^^^ keyword.control.loop.for.liquid
|                               ^^^^^^^^ variable.other.liquid
|                                        ^^ keyword.operator.assignment.liquid
|                                           ^^^^^^^ variable.other.liquid
|                                                   ^^ punctuation.definition.tag.end.liquid

{% style %}
| <- meta.tag.liquid punctuation.definition.tag.schema.begin.liquid
|^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.schema.begin.liquid
|  ^^^^^ keyword.declaration.raw.liquid
|        ^^ punctuation.definition.tag.schema.end.liquid

div {
    font-{{family}}: "{{font}}";
|        ^^^^^^^^^^ meta.property-list.css meta.block.css meta.object.liquid
|        ^^ punctuation.definition.object.begin.liquid
|          ^^^^^^ variable.other.liquid
|                ^^ punctuation.definition.object.end.liquid
|                    ^ meta.string.css string.quoted.double.css punctuation.definition.string.begin.css
|                     ^^^^^^^^ meta.property-list.css meta.block.css meta.property-value.css meta.string.css meta.interpolation.liquid meta.object.liquid
|                     ^^ punctuation.definition.object.begin.liquid
|                       ^^^^ variable.other.liquid
|                           ^^ punctuation.definition.object.end.liquid
|                             ^ meta.string.css string.quoted.double.css punctuation.definition.string.end.css
}

{% endstyle %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^^^^^ keyword.declaration.raw.liquid
|           ^^ punctuation.definition.tag.end.liquid


<!--
 --- Test Objects
 -->

  {{ foo.bar | where: "foo" }}
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.object.liquid
| ^^ punctuation.definition.object.begin.liquid
|    ^^^ variable.other.liquid
|       ^ punctuation.accessor.dot.liquid
|        ^^^ variable.other.member.liquid
|            ^ keyword.operator.logical.pipe.liquid
|              ^^^^^ support.function.filter.liquid
|                   ^ punctuation.separator.key-value.liquid
|                     ^^^^^ meta.string.liquid string.quoted.double.liquid
|                           ^^ punctuation.definition.object.end.liquid

  {{ 10 -10 +10 }}
| ^^^^^^^^^^^^^^^^ meta.object.liquid
|    ^^ meta.number.integer.decimal.liquid constant.numeric.value.liquid
|       ^^^ meta.number.integer.decimal.liquid constant.numeric.value.liquid
|       ^ keyword.operator.arithmetic.liquid
|           ^^^ meta.number.integer.decimal.liquid constant.numeric.value.liquid
|           ^ keyword.operator.arithmetic.liquid

  {{ 0.1 -0.1 +0.1 }}
| ^^^^^^^^^^^^^^^^^^^ meta.object.liquid
|    ^^^ meta.number.float.decimal.liquid constant.numeric.value.liquid
|     ^ punctuation.separator.decimal.liquid
|        ^^^^ meta.number.float.decimal.liquid constant.numeric.value.liquid
|        ^ keyword.operator.arithmetic.liquid
|          ^ punctuation.separator.decimal.liquid
|             ^^^^ meta.number.float.decimal.liquid constant.numeric.value.liquid
|             ^ keyword.operator.arithmetic.liquid
|               ^ punctuation.separator.decimal.liquid

  {{ site.users[1] }}
| ^^^^^^^^^^^^^^^^^^^ meta.object.liquid
|              ^^^ meta.item-access.liquid meta.brackets.liquid
|              ^ punctuation.section.brackets.begin.liquid
|               ^ meta.number.integer.decimal.liquid constant.numeric.value.liquid
|                ^ punctuation.section.brackets.end.liquid

  {{ site.users[-1] }}
| ^^^^^^^^^^^^^^^^^^^^ meta.object.liquid
|              ^^^^ meta.item-access.liquid meta.brackets.liquid
|              ^ punctuation.section.brackets.begin.liquid
|               ^^ meta.number.integer.decimal.liquid constant.numeric.value.liquid
|                 ^ punctuation.section.brackets.end.liquid

  {{ site.users[index] }}
| ^^^^^^^^^^^^^^^^^^^^^^^ meta.object.liquid
|              ^^^^^^^ meta.item-access.liquid meta.brackets.liquid
|              ^ punctuation.section.brackets.begin.liquid
|               ^^^^^ variable.other.liquid
|                    ^ punctuation.section.brackets.end.liquid

  {{ site.users["index"] }}
| ^^^^^^^^^^^^^^^^^^^^^^^^^ meta.object.liquid
|              ^^^^^^^^^ meta.item-access.liquid meta.brackets.liquid
|              ^ punctuation.section.brackets.begin.liquid
|               ^^^^^^^ meta.string.liquid string.quoted.double.liquid
|                      ^ punctuation.section.brackets.end.liquid


<!--
 --- Test HTML
 -->

<div attrib="{{obj}}">
|            ^^^^^^^ meta.tag.block.any.html meta.attribute-with-value.html meta.string.html meta.interpolation.liquid meta.object.liquid
    {% if true %}
|   ^^^^^^^^^^^^^ meta.tag.liquid
    A Paragraph {{var}}
|               ^^^^^^^ meta.object.liquid
    {% endif %}
|   ^^^^^^^^^^^ meta.tag.liquid
</div>
|^^^^^ meta.tag.block.any.html


<!--
 --- Test CSS
 -->

<style>
    hr {
        {% if true %}
|       ^^^^^^^^^^^^^ source.css.embedded.html meta.property-list.css meta.block.css meta.tag.liquid
|       ^^ punctuation.definition.tag.begin.liquid
|          ^^ keyword.control.conditional.if.liquid
|             ^^^^ constant.language.boolean.liquid
|                  ^^ punctuation.definition.tag.end.liquid
        font-{{family}}: "{{font}}";
|            ^^^^^^^^^^ source.css.embedded.html meta.property-list.css meta.block.css meta.object.liquid
|            ^^ punctuation.definition.object.begin.liquid
|              ^^^^^^ variable.other.liquid
|                    ^^ punctuation.definition.object.end.liquid
|                        ^ meta.string.css string.quoted.double.css punctuation.definition.string.begin.css
|                         ^^^^^^^^ source.css.embedded.html meta.property-list.css meta.block.css meta.property-value.css meta.string.css meta.interpolation.liquid meta.object.liquid
|                         ^^ punctuation.definition.object.begin.liquid
|                           ^^^^ variable.other.liquid
|                               ^^ punctuation.definition.object.end.liquid
|                                 ^ meta.string.css string.quoted.double.css punctuation.definition.string.end.css
        {% endif %}
|       ^^^^^^^^^^^ source.css.embedded.html meta.property-list.css meta.block.css meta.tag.liquid
|       ^^ punctuation.definition.tag.begin.liquid
|          ^^^^^ keyword.control.conditional.end.liquid
|                ^^ punctuation.definition.tag.end.liquid
    }
</style>


<!--
 --- Test JavaScript
 -->

<script>
    function foo({{args_list}}) {
|                ^^^^^^^^^^^^^ source.js.embedded.html meta.function.parameters.js meta.object.liquid
        {% for i in vars %}
|       ^^^^^^^^^^^^^^^^^^^ source.js.embedded.html meta.function.js meta.block.js meta.tag.liquid
        {% endfor %}
|       ^^^^^^^^^^^^ source.js.embedded.html meta.function.js meta.block.js meta.tag.liquid
    }
|   ^ source.js.embedded.html meta.function.js meta.block.js punctuation.section.block.end.js
</script>
