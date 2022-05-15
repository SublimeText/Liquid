| SYNTAX TEST "Packages/Liquid/Syntaxes/Markdown (Jekyll).sublime-syntax"

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


<!-- Jekyll Spcific Tags -->

[Link to a {{file}}]({% link /assets/files/doc.pdf %})
| <- meta.paragraph.markdown meta.link.inline.description.markdown punctuation.definition.link.begin.markdown
|^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown meta.link.inline.description.markdown
|          ^^^^^^^^ meta.object.liquid
|          ^^ punctuation.definition.object.begin.liquid
|            ^^^^ variable.other.liquid
|                ^^ punctuation.definition.object.end.liquid
|                  ^ punctuation.definition.link.end.markdown
|                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown meta.link.inline.metadata.markdown
|                   ^ punctuation.definition.metadata.begin.markdown
|                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|                    ^^ punctuation.definition.tag.begin.liquid
|                       ^^^^ keyword.declaration.link.liquid.jekyll
|                            ^^^^^^^^^^^^^^^^^^^^^ meta.path.url.html meta.string.html string.unquoted.html
|                                                  ^^ punctuation.definition.tag.end.liquid
|                                                    ^ punctuation.definition.metadata.end.markdown

{% link {{myvar}} %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^ keyword.declaration.link.liquid.jekyll
|       ^^^^^^^^^ meta.path.url.html meta.string.html meta.interpolation.liquid meta.object.liquid
|       ^^ punctuation.definition.object.begin.liquid
|         ^^^^^ variable.other.liquid
|              ^^ punctuation.definition.object.end.liquid
|                 ^^ punctuation.definition.tag.end.liquid

{% link mypage.html | append: "#section1" %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^ keyword.declaration.link.liquid.jekyll
|       ^^^^^^^^^^^ meta.path.url.html meta.string.html string.unquoted.html
|                   ^ keyword.operator.logical.pipe.liquid
|                     ^^^^^^ support.function.filter.liquid
|                           ^ punctuation.separator.key-value.liquid
|                             ^^^^^^^^^^^ meta.string.liquid string.quoted.double.liquid
|                                         ^^ punctuation.definition.tag.end.liquid

{% post_url 2010-07-21-name-of-post %}
| <- meta.tag.liquid punctuation.definition.tag.begin.liquid
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag.liquid
|^ punctuation.definition.tag.begin.liquid
|  ^^^^^^^^ keyword.declaration.link.liquid.jekyll
|           ^^^^^^^^^^^^^^^^^^^^^^^ meta.path.url.html meta.string.html string.unquoted.html
|                                   ^^ punctuation.definition.tag.end.liquid


<!-- Jekyll Highlight Tags -->

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
