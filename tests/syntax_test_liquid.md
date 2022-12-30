| SYNTAX TEST "Packages/Liquid/Syntaxes/Markdown (Liquid).sublime-syntax"

<!--
 --- Test Liquid Control Flow
 --- https://shopify.github.io/liquid/tags/control-flow
 -->

{% if true %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^ keyword.control.conditional.if.liquid
|     ^^^^ constant.language.boolean.liquid
|          ^^ punctuation.section.embedded.end.liquid

A Paragraph {{var}}
|           ^^^^^^^ meta.interpolation.liquid

{% elsif foo %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^ keyword.control.conditional.elseif.liquid
|        ^^^ variable.other.liquid
|            ^^ punctuation.section.embedded.end.liquid

{% else %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^ keyword.control.conditional.else.liquid
|       ^^ punctuation.section.embedded.end.liquid

{% endif %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^ keyword.control.conditional.end.liquid
|        ^^ punctuation.section.embedded.end.liquid

{% if product.tags contains "Hello" %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^ keyword.control.conditional.if.liquid
|     ^^^^^^^ variable.other.liquid
|            ^ punctuation.accessor.dot.liquid
|             ^^^^ variable.other.member.liquid
|                  ^^^^^^^^ keyword.operator.logical.liquid
|                           ^^^^^^^ meta.string.liquid string.quoted.double.liquid
|                                   ^^ punctuation.section.embedded.end.liquid

{% case handle %}
|^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|  ^^^^ keyword.control.conditional.case.liquid
|       ^^^^^^ variable.other.liquid
  {% when "cake" %}
| ^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|    ^^^^ keyword.control.conditional.when.liquid
|         ^^^^^^ meta.string.liquid string.quoted.double.liquid
     This is a cake
  {% when "cookie", "biscuit" %}
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|    ^^^^ keyword.control.conditional.when.liquid
|         ^^^^^^^^ meta.string.liquid string.quoted.double.liquid
|                 ^ punctuation.separator.sequence.liquid
|                   ^^^^^^^^^ meta.string.liquid string.quoted.double.liquid
     This is a cookie
  {% else %}
| ^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|    ^^^^ keyword.control.conditional.else.liquid
     This is not a cake nor a cookie
{% endcase %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|  ^^^^^^^ keyword.control.conditional.end.liquid

{% liquid
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^^ keyword.declaration.liquid

case section.blocks.size
| <- meta.embedded.liquid source.liquid meta.statement.liquid keyword.control.conditional.case.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid

when 1
| <- meta.embedded.liquid source.liquid meta.statement.liquid keyword.control.conditional.when.liquid
|^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^^^ keyword.control.conditional.when.liquid
|    ^ constant.numeric.value.liquid

  assign column_size = ''
|^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
| ^^^^^^ keyword.control.liquid
|        ^^^^^^^^^^^ variable.other.liquid
|                    ^ keyword.operator.assignment.liquid
|                      ^^ meta.string.liquid string.quoted.single.liquid

when 2
| <- meta.embedded.liquid source.liquid meta.statement.liquid keyword.control.conditional.when.liquid

  assign column_size = 'one-half'
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
| ^^^^^^ keyword.control.liquid
|        ^^^^^^^^^^^ variable.other.liquid
|                    ^ keyword.operator.assignment.liquid
|                      ^^^^^^^^^^ meta.string.liquid string.quoted.single.liquid

else
| <- meta.embedded.liquid source.liquid meta.statement.liquid keyword.control.conditional.else.liquid

  assign column_size = 'one-quarter'
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
| ^^^^^^ keyword.control.liquid
|        ^^^^^^^^^^^ variable.other.liquid
|                    ^ keyword.operator.assignment.liquid
|                      ^^^^^^^^^^^^^ meta.string.liquid string.quoted.single.liquid

endcase %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid keyword.control.conditional.end.liquid
|^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^^^^^^ keyword.control.conditional.end.liquid
|       ^^ punctuation.section.embedded.end.liquid


<!--
 --- Test Iteration Statements
 --- https://shopify.github.io/liquid/tags/iteration/
-->

{% for %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|  ^^^ keyword.control.loop.for.liquid

{% for item in array limit:2 %}
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|                    ^^^^^ variable.parameter.loop.liquid
|                         ^ punctuation.separator.key-value.liquid
|                          ^ constant.numeric.value.liquid

{% for item in array offset:2 %}
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|                    ^^^^^^ variable.parameter.loop.liquid
|                          ^ punctuation.separator.key-value.liquid
|                           ^ constant.numeric.value.liquid

{% for item in array reversed %}
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|                    ^^^^^^^^ variable.parameter.loop.liquid

{% for i in (1..5) %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|  ^^^ keyword.control.loop.for.liquid
|      ^ variable.other.liquid
|        ^^ keyword.operator.logical.liquid
|           ^^^^^^ meta.sequence.range.liquid
|           ^ punctuation.section.sequence.begin.liquid
|            ^ constant.numeric.value.liquid
|             ^^ punctuation.separator.range.liquid
|               ^ constant.numeric.value.liquid
|                ^ punctuation.section.sequence.end.liquid
|                  ^^ punctuation.section.embedded.end.liquid

{% for i in (1..num) %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|  ^^^ keyword.control.loop.for.liquid
|      ^ variable.other.liquid
|        ^^ keyword.operator.logical.liquid
|           ^^^^^^^^ meta.sequence.range.liquid
|           ^ punctuation.section.sequence.begin.liquid
|            ^ constant.numeric.value.liquid
|             ^^ punctuation.separator.range.liquid
|               ^^^ variable.other.liquid
|                  ^ punctuation.section.sequence.end.liquid
|                    ^^ punctuation.section.embedded.end.liquid

{% for product in collection.products %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^ keyword.control.loop.for.liquid
|      ^^^^^^^ variable.other.liquid
|              ^^ keyword.operator.logical.liquid
|                 ^^^^^^^^^^ variable.other.liquid
|                           ^ punctuation.accessor.dot.liquid
|                            ^^^^^^^^ variable.other.member.liquid
|                                     ^^ punctuation.section.embedded.end.liquid

  {% cycle "one", "two", "three" %}
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
| ^^ punctuation.section.embedded.begin.liquid
|    ^^^^^ support.function.cycle.liquid
|          ^^^^^ meta.string.liquid string.quoted.double.liquid
|               ^ punctuation.separator.sequence.liquid
|                 ^^^^^ meta.string.liquid string.quoted.double.liquid
|                      ^ punctuation.separator.sequence.liquid
|                        ^^^^^^^ meta.string.liquid string.quoted.double.liquid
|                                ^^ punctuation.section.embedded.end.liquid

  {% cycle "first": "one", "two", "three" %}
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
| ^^ punctuation.section.embedded.begin.liquid
|    ^^^^^ support.function.cycle.liquid
|          ^^^^^^^ constant.other.group.liquid
|          ^ punctuation.definition.constant.begin.liquid
|                ^ punctuation.definition.constant.end.liquid
|                 ^ punctuation.separator.key-value.liquid
|                   ^^^^^ meta.string.liquid string.quoted.double.liquid
|                        ^ punctuation.separator.sequence.liquid

  {% cycle 'first': 'one', 'two', 'three' %}
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
| ^^ punctuation.section.embedded.begin.liquid
|    ^^^^^ support.function.cycle.liquid
|          ^^^^^^^ constant.other.group.liquid
|          ^ punctuation.definition.constant.begin.liquid
|                ^ punctuation.definition.constant.end.liquid
|                 ^ punctuation.separator.key-value.liquid
|                   ^^^^^ meta.string.liquid string.quoted.single.liquid
|                        ^ punctuation.separator.sequence.liquid

  {% break %}
| ^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
| ^^ punctuation.section.embedded.begin.liquid
|    ^^^^^ keyword.control.flow.break.liquid
|          ^^ punctuation.section.embedded.end.liquid

{% else %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^ keyword.control.conditional.else.liquid
|       ^^ punctuation.section.embedded.end.liquid

  {% continue %}
| ^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
| ^^ punctuation.section.embedded.begin.liquid
|    ^^^^^^^^ keyword.control.flow.continue.liquid
|             ^^ punctuation.section.embedded.end.liquid

{% endfor %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^^ keyword.control.loop.end.liquid
|         ^^ punctuation.section.embedded.end.liquid

{% tablerow product in (1..collection.products) cols:4 limit:5 offset:1 %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
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
|                                                                       ^^ punctuation.section.embedded.end.liquid

{% endtablerow %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^^^^^^^ keyword.control.loop.end.liquid
|              ^^ punctuation.section.embedded.end.liquid

{% liquid
for product in collection.products
| <- meta.embedded.liquid source.liquid meta.statement.liquid keyword.control.loop.for.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^^ keyword.control.loop.for.liquid
|   ^^^^^^^ variable.other.liquid
|           ^^ keyword.operator.logical.liquid
|              ^^^^^^^^^^ variable.other.liquid
|                        ^ punctuation.accessor.dot.liquid
|                         ^^^^^^^^ variable.other.member.liquid
  echo product.title | capitalize
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
| ^^^^ support.function.liquid
|      ^^^^^^^ variable.other.liquid
|             ^ punctuation.accessor.dot.liquid
|              ^^^^^ variable.other.member.liquid
|                    ^ keyword.operator.logical.pipe.liquid
|                      ^^^^^^^^^^ support.function.filter.liquid
endfor %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid keyword.control.loop.end.liquid
|^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^^^^^ keyword.control.loop.end.liquid
|      ^^ punctuation.section.embedded.end.liquid

<!--
 --- Variable Statements
 --- https://shopify.github.io/liquid/tags/variable
 -->

{% assign handle = "cake" %}
|^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|  ^^^^^^ keyword.control.liquid
|         ^^^^^^ variable.other.liquid
|                ^ keyword.operator.assignment.liquid
|                  ^^^^^^ meta.string.liquid string.quoted.double.liquid

{% assign foo = bar | where: "type", "baz" %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
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
|                                          ^^ punctuation.section.embedded.end.liquid

{% capture about_me %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^^^ keyword.control.liquid
|          ^^^^^^^^ variable.other.liquid
|                   ^^ punctuation.section.embedded.end.liquid

I am {{ age }} and my favorite food is {{ favorite_food }}.
|    ^^^^^^^^^ meta.interpolation.liquid
|                                      ^^^^^^^^^^^^^^^^^^^ meta.interpolation.liquid

{% endcapture %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^^^^^^ keyword.control.liquid
|             ^^ punctuation.section.embedded.end.liquid

{% increment my_counter %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^^^^^ support.function.liquid
|            ^^^^^^^^^^ variable.other.liquid
|                       ^^ punctuation.section.embedded.end.liquid

{% decrement my_counter %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^^^^^ support.function.liquid
|            ^^^^^^^^^^ variable.other.liquid
|                       ^^ punctuation.section.embedded.end.liquid


<!--
 --- Template Tests
 --- https://shopify.github.io/liquid/tags/template
 -->

{% comment %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^^^ keyword.declaration.comment.liquid
|          ^^ punctuation.section.embedded.end.liquid

{% assign verb = "converted" %}
| <- meta.embedded.liquid source.liquid comment.block.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid comment.block.liquid

{% endcomment %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^^^^^^ keyword.declaration.comment.liquid
|             ^^ punctuation.section.embedded.end.liquid

{% javascript %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^^^^^^ keyword.declaration.raw.liquid
|             ^^ punctuation.section.embedded.end.liquid
  function foo() { return 0; }
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ source.js.embedded.liquid
{% endjavascript %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^^^^^^^^^ keyword.declaration.raw.liquid
|                ^^ punctuation.section.embedded.end.liquid

{% raw %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^ keyword.declaration.raw.liquid
|      ^^ punctuation.section.embedded.end.liquid

In Handlebars, {{ this }} will be HTML-escaped, but {{{ that }}} will not.
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.raw.liquid
|              ^^^^^^^^^^ - meta.interpolation.liquid
|                                                   ^^^^^^^^^^^^ - meta.interpolation.liquid

{% raw %}
|^^^^^^^^^ meta.raw.liquid - meta.tag - punctuation - keyword

{% endraw %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^^ keyword.declaration.raw.liquid
|         ^^ punctuation.section.embedded.end.liquid

{% include "template-name" %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^^^ keyword.control.import.liquid
|          ^^^^^^^^^^^^^^^ meta.string.liquid string.quoted.double.liquid
|                          ^^ punctuation.section.embedded.end.liquid

{% render "product", product: featured_product %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^^ support.function.liquid
|         ^^^^^^^^^ meta.string.liquid string.quoted.double.liquid
|                  ^ punctuation.separator.sequence.liquid
|                    ^^^^^^^ variable.parameter.liquid
|                           ^ punctuation.separator.key-value.liquid
|                             ^^^^^^^^^^^^^^^^ variable.other.liquid
|                                              ^^ punctuation.section.embedded.end.liquid

{% render "product" with featured_product as product %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^^ support.function.liquid
|         ^^^^^^^^^ meta.string.liquid string.quoted.double.liquid
|                   ^^^^ keyword.declaration.with.liquid
|                        ^^^^^^^^^^^^^^^^ variable.other.liquid
|                                         ^^ keyword.operator.assignment.liquid
|                                            ^^^^^^^ variable.other.liquid
|                                                    ^^ punctuation.section.embedded.end.liquid

{% render "product_variant" for variants as variant %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^^ support.function.liquid
|         ^^^^^^^^^^^^^^^^^ meta.string.liquid string.quoted.double.liquid
|                           ^^^ keyword.control.loop.for.liquid
|                               ^^^^^^^^ variable.other.liquid
|                                        ^^ keyword.operator.assignment.liquid
|                                           ^^^^^^^ variable.other.liquid
|                                                   ^^ punctuation.section.embedded.end.liquid

{% layout 'full-width' %}
|<- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^^ keyword.declaration.layout.liquid
|         ^^^^^^^^^^^^ meta.string.liquid string.quoted.single.liquid
|                      ^^ punctuation.section.embedded.end.liquid

{% form 'reset_customer_password' %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^ keyword.declaration.form.liquid
|       ^^^^^^^^^^^^^^^^^^^^^^^^^ meta.string.liquid string.quoted.single.liquid
|                                 ^^ punctuation.section.embedded.end.liquid

{% endform %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^^^ keyword.declaration.form.liquid
|          ^^ punctuation.section.embedded.end.liquid

{% section 'section' %}
|<- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^^^ keyword.declaration.section.liquid
|          ^^^^^^^^^ meta.string.liquid string.quoted.single.liquid
|                    ^^ punctuation.section.embedded.end.liquid

{% paginate section.settings.products by 2 %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^^^^ keyword.control.paginate.liquid
|                                     ^^ keyword.operator.liquid
|                                        ^ meta.number.integer.decimal.liquid constant.numeric.value.liquid
|                                          ^^ punctuation.section.embedded.end.liquid

{% endpaginate %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^^^^^^^ keyword.control.paginate.liquid
|              ^^ punctuation.section.embedded.end.liquid

{% style %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^ keyword.declaration.raw.liquid
|        ^^ punctuation.section.embedded.end.liquid

div {
    font-{{family}}: "{{font}}";
|        ^^^^^^^^^^ meta.property-list.css meta.block.css meta.interpolation.liquid
|        ^^ punctuation.section.interpolation.begin.liquid
|          ^^^^^^ variable.other.liquid
|                ^^ punctuation.section.interpolation.end.liquid
|                    ^ meta.string.css string.quoted.double.css punctuation.definition.string.begin.css
|                     ^^^^^^^^ meta.property-list.css meta.block.css meta.property-value.css meta.string.css meta.interpolation.liquid
|                     ^^ punctuation.section.interpolation.begin.liquid
|                       ^^^^ variable.other.liquid
|                           ^^ punctuation.section.interpolation.end.liquid
|                             ^ meta.string.css string.quoted.double.css punctuation.definition.string.end.css
}

{% endstyle %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^^^^ keyword.declaration.raw.liquid
|           ^^ punctuation.section.embedded.end.liquid

{% plugin "foo" %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^^ keyword.other.liquid
|         ^^^^^ meta.string.liquid string.quoted.double.liquid
|               ^^ punctuation.section.embedded.end.liquid


<!--
 --- Test Objects
 -->

  {{ foo.bar | where: "foo" }}
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.interpolation.liquid
| ^^ punctuation.section.interpolation.begin.liquid
|    ^^^ variable.other.liquid
|       ^ punctuation.accessor.dot.liquid
|        ^^^ variable.other.member.liquid
|            ^ keyword.operator.logical.pipe.liquid
|              ^^^^^ support.function.filter.liquid
|                   ^ punctuation.separator.key-value.liquid
|                     ^^^^^ meta.string.liquid string.quoted.double.liquid
|                           ^^ punctuation.section.interpolation.end.liquid

  {{ 10 -10 +10 }}
| ^^^^^^^^^^^^^^^^ meta.interpolation.liquid
|    ^^ meta.number.integer.decimal.liquid constant.numeric.value.liquid
|       ^^^ meta.number.integer.decimal.liquid constant.numeric.value.liquid
|       ^ keyword.operator.arithmetic.liquid
|           ^^^ meta.number.integer.decimal.liquid constant.numeric.value.liquid
|           ^ keyword.operator.arithmetic.liquid

  {{ 0.1 -0.1 +0.1 }}
| ^^^^^^^^^^^^^^^^^^^ meta.interpolation.liquid
|    ^^^ meta.number.float.decimal.liquid constant.numeric.value.liquid
|     ^ punctuation.separator.decimal.liquid
|        ^^^^ meta.number.float.decimal.liquid constant.numeric.value.liquid
|        ^ keyword.operator.arithmetic.liquid
|          ^ punctuation.separator.decimal.liquid
|             ^^^^ meta.number.float.decimal.liquid constant.numeric.value.liquid
|             ^ keyword.operator.arithmetic.liquid
|               ^ punctuation.separator.decimal.liquid

  {{ site.users[1] }}
| ^^^^^^^^^^^^^^^^^^^ meta.interpolation.liquid
|              ^^^ meta.item-access.liquid meta.brackets.liquid
|              ^ punctuation.section.brackets.begin.liquid
|               ^ meta.number.integer.decimal.liquid constant.numeric.value.liquid
|                ^ punctuation.section.brackets.end.liquid

  {{ site.users[-1] }}
| ^^^^^^^^^^^^^^^^^^^^ meta.interpolation.liquid
|              ^^^^ meta.item-access.liquid meta.brackets.liquid
|              ^ punctuation.section.brackets.begin.liquid
|               ^^ meta.number.integer.decimal.liquid constant.numeric.value.liquid
|                 ^ punctuation.section.brackets.end.liquid

  {{ site.users[index] }}
| ^^^^^^^^^^^^^^^^^^^^^^^ meta.interpolation.liquid
|              ^^^^^^^ meta.item-access.liquid meta.brackets.liquid
|              ^ punctuation.section.brackets.begin.liquid
|               ^^^^^ variable.other.liquid
|                    ^ punctuation.section.brackets.end.liquid

  {{ site.users["index"] }}
| ^^^^^^^^^^^^^^^^^^^^^^^^^ meta.interpolation.liquid
|              ^^^^^^^^^ meta.item-access.liquid meta.brackets.liquid
|              ^ punctuation.section.brackets.begin.liquid
|               ^^^^^^^ meta.string.liquid string.quoted.double.liquid
|                      ^ punctuation.section.brackets.end.liquid


<!--
 --- Test HTML
 -->

<div attrib="{{obj}}">
|            ^^^^^^^ meta.tag.block.any.html meta.attribute-with-value.html meta.string.html meta.interpolation.liquid
    {% if true %}
|   ^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
    A Paragraph {{var}}
|               ^^^^^^^ meta.interpolation.liquid
    {% endif %}
|   ^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
</div>
|^^^^^ meta.tag.block.any.html


<!--
 --- Test CSS
 -->

<style>
    hr {
        {% if true %}
|       ^^^^^^^^^^^^^ source.css.embedded.html meta.property-list.css meta.block.css meta.embedded.liquid source.liquid meta.statement.liquid
|       ^^ punctuation.section.embedded.begin.liquid
|          ^^ keyword.control.conditional.if.liquid
|             ^^^^ constant.language.boolean.liquid
|                  ^^ punctuation.section.embedded.end.liquid
        font-{{family}}: "{{font}}";
|            ^^^^^^^^^^ source.css.embedded.html meta.property-list.css meta.block.css meta.interpolation.liquid
|            ^^ punctuation.section.interpolation.begin.liquid
|              ^^^^^^ variable.other.liquid
|                    ^^ punctuation.section.interpolation.end.liquid
|                        ^ meta.string.css string.quoted.double.css punctuation.definition.string.begin.css
|                         ^^^^^^^^ source.css.embedded.html meta.property-list.css meta.block.css meta.property-value.css meta.string.css meta.interpolation.liquid
|                         ^^ punctuation.section.interpolation.begin.liquid
|                           ^^^^ variable.other.liquid
|                               ^^ punctuation.section.interpolation.end.liquid
|                                 ^ meta.string.css string.quoted.double.css punctuation.definition.string.end.css
        {% endif %}
|       ^^^^^^^^^^^ source.css.embedded.html meta.property-list.css meta.block.css meta.embedded.liquid source.liquid meta.statement.liquid
|       ^^ punctuation.section.embedded.begin.liquid
|          ^^^^^ keyword.control.conditional.end.liquid
|                ^^ punctuation.section.embedded.end.liquid
    }
</style>


<!--
 --- Test JavaScript
 -->

<script>
    function foo({{args_list}}) {
|                ^^^^^^^^^^^^^ source.js.embedded.html meta.function.parameters.js meta.interpolation.liquid
        {% for i in vars %}
|       ^^^^^^^^^^^^^^^^^^^ source.js.embedded.html meta.function.js meta.block.js meta.embedded.liquid source.liquid meta.statement.liquid
        {% endfor %}
|       ^^^^^^^^^^^^ source.js.embedded.html meta.function.js meta.block.js meta.embedded.liquid source.liquid meta.statement.liquid
    }
|   ^ source.js.embedded.html meta.function.js meta.block.js punctuation.section.block.end.js
</script>
