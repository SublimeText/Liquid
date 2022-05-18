| SYNTAX TEST "Packages/Liquid/Syntaxes/Markdown (Liquid).sublime-syntax"

{% link https://%}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^ keyword.declaration.link.liquid.jekyll
|       ^^^^^^^^ meta.path.url.liquid meta.string.liquid string.unquoted.liquid
|            ^^^ punctuation.separator.path.liquid
|               ^^ punctuation.definition.tag.end.liquid

{% link https://foo.bar/baz %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^ keyword.declaration.link.liquid.jekyll
|       ^^^^^^^^^^^^^^^^^^^ meta.path.url.liquid meta.string.liquid string.unquoted.liquid
|            ^^^ punctuation.separator.path.liquid
|                      ^ punctuation.separator.path.liquid
|                           ^^ punctuation.definition.tag.end.liquid

{% link 'https://foo.bar/baz' %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^ keyword.declaration.link.liquid.jekyll
|       ^ meta.string.liquid string.quoted.single.liquid punctuation.definition.string.begin.liquid
|        ^^^^^^^^^^^^^^^^^^^ meta.path.url.liquid meta.string.liquid string.quoted.single.liquid
|             ^^^ punctuation.separator.path.liquid
|                       ^ punctuation.separator.path.liquid
|                           ^ meta.string.liquid string.quoted.single.liquid punctuation.definition.string.end.liquid
|                             ^^ punctuation.definition.tag.end.liquid

{% link "https://foo.bar/baz" %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^ keyword.declaration.link.liquid.jekyll
|       ^ meta.string.liquid string.quoted.double.liquid punctuation.definition.string.begin.liquid
|        ^^^^^^^^^^^^^^^^^^^ meta.path.url.liquid meta.string.liquid string.quoted.double.liquid
|             ^^^ punctuation.separator.path.liquid
|                       ^ punctuation.separator.path.liquid
|                           ^ meta.string.liquid string.quoted.single.liquid punctuation.definition.string.end.liquid
|                             ^^ punctuation.definition.tag.end.liquid

{% link {{ page.my_variable }} %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^ keyword.declaration.link.liquid.jekyll
|       ^^^^^^^^^^^^^^^^^^^^^^ meta.path.url.liquid meta.string.liquid meta.interpolation.liquid meta.object.liquid
|       ^^ punctuation.definition.object.begin.liquid
|          ^^^^ variable.other.liquid
|              ^ punctuation.accessor.dot.liquid
|               ^^^^^^^^^^^ variable.other.liquid
|                           ^^ punctuation.definition.object.end.liquid
|                              ^^ punctuation.definition.tag.end.liquid

{% post_url https://foo.bar/baz %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^^^^^ keyword.declaration.link.liquid.jekyll
|           ^^^^^^^^^^^^^^^^^^^ meta.path.url.liquid meta.string.liquid string.unquoted.liquid
|                               ^^ punctuation.definition.tag.end.liquid

{% highlight raw %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^^^^^^ keyword.declaration.highlight.liquid.jekyll
|            ^^^ constant.other.language-name.liquid.jekyll
|                ^^ punctuation.definition.tag.end.liquid
|                  ^ - meta.tag - markup - source
def foo
  puts 'foo'
|^^^^^^^^^^^^ markup.raw.code-fence.liquid.jekyll
end
{% endhighlight %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^^^^^^^^^ keyword.declaration.highlight.liquid.jekyll
|               ^^ punctuation.definition.tag.end.liquid

{% highlight ruby %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^^^^^^ keyword.declaration.highlight.liquid.jekyll
|            ^^^^ constant.other.language-name.liquid.jekyll
|                 ^^ punctuation.definition.tag.end.liquid
|                   ^ - meta.tag - markup - source
def foo
| <- markup.raw.code-fence.liquid.jekyll source.ruby.embedded.liquid.jekyll meta.function.ruby keyword.declaration.function.ruby
  puts 'foo'
| ^^^^ markup.raw.code-fence.liquid.jekyll source.ruby.embedded.liquid.jekyll support.function.builtin.ruby
end
| <- markup.raw.code-fence.liquid.jekyll source.ruby.embedded.liquid.jekyll keyword.control.block.end.ruby
{% endhighlight %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^^^^^^^^^ keyword.declaration.highlight.liquid.jekyll
|               ^^ punctuation.definition.tag.end.liquid


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