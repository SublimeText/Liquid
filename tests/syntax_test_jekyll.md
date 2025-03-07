| SYNTAX TEST "Packages/Liquid/Syntaxes/Markdown (Liquid).sublime-syntax"

{% link https://%}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^ keyword.declaration.link.liquid.jekyll
|       ^^^^^^^^ meta.path.url.liquid meta.string.liquid string.unquoted.liquid
|            ^^^ punctuation.separator.path.liquid
|               ^^ punctuation.section.embedded.end.liquid

{% link https://foo.bar/baz %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^ keyword.declaration.link.liquid.jekyll
|       ^^^^^^^^^^^^^^^^^^^ meta.path.url.liquid meta.string.liquid string.unquoted.liquid
|            ^^^ punctuation.separator.path.liquid
|                      ^ punctuation.separator.path.liquid
|                           ^^ punctuation.section.embedded.end.liquid

{% link 'https://foo.bar/baz' %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^ keyword.declaration.link.liquid.jekyll
|       ^ meta.string.liquid string.quoted.single.liquid punctuation.definition.string.begin.liquid
|        ^^^^^^^^^^^^^^^^^^^ meta.path.url.liquid meta.string.liquid string.quoted.single.liquid
|             ^^^ punctuation.separator.path.liquid
|                       ^ punctuation.separator.path.liquid
|                           ^ meta.string.liquid string.quoted.single.liquid punctuation.definition.string.end.liquid
|                             ^^ punctuation.section.embedded.end.liquid

{% link "https://foo.bar/baz" %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^ keyword.declaration.link.liquid.jekyll
|       ^ meta.string.liquid string.quoted.double.liquid punctuation.definition.string.begin.liquid
|        ^^^^^^^^^^^^^^^^^^^ meta.path.url.liquid meta.string.liquid string.quoted.double.liquid
|             ^^^ punctuation.separator.path.liquid
|                       ^ punctuation.separator.path.liquid
|                           ^ meta.string.liquid string.quoted.single.liquid punctuation.definition.string.end.liquid
|                             ^^ punctuation.section.embedded.end.liquid

{% link {{ page.my_variable }} %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^ keyword.declaration.link.liquid.jekyll
|       ^^^^^^^^^^^^^^^^^^^^^^ meta.path.url.liquid meta.string.liquid meta.interpolation.liquid
|       ^^ punctuation.section.interpolation.begin.liquid
|          ^^^^ variable.language.globals.jekyll
|              ^ punctuation.accessor.dot.liquid
|               ^^^^^^^^^^^ variable.other.member.liquid
|                           ^^ punctuation.section.interpolation.end.liquid
|                              ^^ punctuation.section.embedded.end.liquid

{% post_url https://foo.bar/baz %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^^^^ keyword.declaration.link.liquid.jekyll
|           ^^^^^^^^^^^^^^^^^^^ meta.path.url.liquid meta.string.liquid string.unquoted.liquid
|                               ^^ punctuation.section.embedded.end.liquid

{% highlight raw %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^^^^^ keyword.declaration.highlight.liquid.jekyll
|            ^^^ constant.other.language-name.liquid.jekyll
|                ^^ punctuation.section.embedded.end.liquid
|                  ^ - meta.tag - markup - source
def foo
  puts 'foo'
|^^^^^^^^^^^^ markup.raw.code-fence.liquid.jekyll
end
{% endhighlight %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^^^^^^^^ keyword.declaration.highlight.liquid.jekyll
|               ^^ punctuation.section.embedded.end.liquid

{% highlight ruby %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^^^^^ keyword.declaration.highlight.liquid.jekyll
|            ^^^^ constant.other.language-name.liquid.jekyll
|                 ^^ punctuation.section.embedded.end.liquid
|                   ^ - meta.tag - markup - source
def foo
| <- markup.raw.code-fence.liquid.jekyll source.ruby.embedded.liquid.jekyll meta.function.ruby keyword.declaration.function.ruby
  puts 'foo'
| ^^^^ markup.raw.code-fence.liquid.jekyll source.ruby.embedded.liquid.jekyll support.function.builtin.ruby
end
| <- markup.raw.code-fence.liquid.jekyll source.ruby.embedded.liquid.jekyll keyword.control.block.end.ruby
{% endhighlight %}
| <- meta.embedded.liquid source.liquid meta.statement.liquid punctuation.section.embedded.begin.liquid
|^^^^^^^^^^^^^^^^^ meta.embedded.liquid source.liquid meta.statement.liquid
|^ punctuation.section.embedded.begin.liquid
|  ^^^^^^^^^^^^ keyword.declaration.highlight.liquid.jekyll
|               ^^ punctuation.section.embedded.end.liquid


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
|             ^^^^ constant.language.boolean.true.liquid
|                  ^^ punctuation.section.embedded.end.liquid
;       font-{{family}}: "{{font}}";
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
