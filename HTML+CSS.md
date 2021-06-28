# HTML



##### Body

```html
<body>...</body>
```

##### Head

```
<head>...</head>
```

##### Header

h1/2/3/4/5...

```html
<h1>Hello World</h1>
```

##### Paragraph

```html
<p>This paragraph is a child of the body element</p>
```

##### Line Breaks

```html
<br>
```

##### Division

“division” or a container that divides the page into sections. 

```html
<div> </div> 
```

##### Main

By using <main> as opposed to a <div> element, screen readers and web browsers are better able to identify that whatever is inside of the tag is the bulk of the content.

```html
<main>
  <header>
    <h1>Types of Sports</h1>
  </header>
  <article>
    <h3>Baseball</h3>
    <p>
      The first game of baseball was played in Cooperstown, New York in the summer of 1839.
    </p>
  </article>
</main>
```

##### Unordered Lists

```html
<ul>...</ul>
```

Ordered Lists

```html
<ol>...</ol>
```

##### Images

```html
<img src="image-location.jpg" />
```

##### Image Alts (alternative text)

```html
<img src="https://content.codecademy.com/courses/web-101/web101-image_brownbear.jpg" alt="Brown Bear"/>
```

##### Videos

```html
<video src="myVideo.mp4" width="320" height="240" controls>
  Video not supported
</video>
```

##### Audio and Attributes

```html
<audio controls>
  <source src="https://content.codecademy.com/courses/SemanticHTML/dogBarking.mp3" type="audio/mp3">
</audio>
```

##### Video and Embed (.gif)

```html
<video src="coding.mp4" controls>Video not supported</video>
<embed src="download.gif"/>
```

##### Links

```html
<a href="https://en.wikipedia.org/wiki/Brown_bear" target="_blank">The Brown Bear</a>
```

##### Linking to Relative Page

```html
<a href="./contact.html">Contact</a>
```

##### Linking to Same Page

```html
 <ul>
    <li><a href="#introduction">Introduction</a></li>
    <li><a href="#habitat">Habitat</a></li>
    <li><a href="#media">Media</a></li>
  </ul>
```

##### Aside Element 

The Aside Element -  additional information that can enhance another element but isn’t required in order to understand the main content. 

```html
<article>
  <p>The first World Series was played between Pittsburgh and Boston in 1903 and was a nine-game series.</p>
</article>
<aside>
  <p>
   Babe Ruth once stated, “Heroes get remembered, but legends never die.” 
  </p>
</aside>
```

##### Figure and Figcaption

```html
<figure>
  <img src="overwatch.jpg">
  <figcaption>This picture shows characters from Overwatch.</figcaption>
</figure>
```

##### Comments

```html
<!-- ______ -->
```

#### TABLE

##### Create a Table

```html
<table>...</table>
```

##### Table Rows

```html
<tr>...</tr>
```

##### Cell element

```html
<td>...</td>
```

##### Table Headings (th)

```html
<table>
  <tr>
    <th></th>
    <th scope="col">Saturday</th>
    <th scope="col">Sunday</th>
  </tr>
  <tr>
    <th scope="row">Temperature</th>
    <td>73</td>
    <td>81</td>
  </tr>
</table>
```

##### Spanning Columns (merge)

```html
<td colspan="2">Out of Town</td>
```

##### Spanning Rows (merge)

```html
<td rowspan="2">Work</td>
```

##### Table Body

```html
<tbody>...</tbody>
```

##### Table Headings

```html
<thead>...</thead>
```

##### Table Footer

The footer contains information such as: 

- Contact information 
- Copyright information 
- Terms of use 
- Site Map 
- Reference to top of page links

```html
<tfoot>
	<p>Contact me at +1 234 567 8910 </p>
</tfoot>
```

#### FORM

##### Text Input

```html
<form action="/example.html" method="POST">
  <input type="text" name="first-text-field">
</form>
```

##### Adding a Label

```html
<label for="meal">What do you want to eat?</label>
```

##### Password Input

```html
<form>
  <label for="user-password">Password: </label>
  <input type="password" id="user-password" name="user-password">
</form>
```

##### Number Input

```html
<form>
  <label for="years"> Years of experience: </label>
  <input id="years" name="years" type="number" step="1">
</form>
```

##### Checkbox Input

```html
<input id="cheese" name="topping" type="checkbox" value="cheese">
 <label for="cheese">Cheese</label>
```

##### Radio Button Input

```html
<input id="yes" type="radio" name="cheese" value="yes">
```

##### Dropdown list

```html
<select id="lunch" name="lunch">
    <option value="pizza">Pizza</option>
    <option value="curry">Curry</option>
    <option value="salad">Salad</option>
```

##### Datalist Input

```html
<input type="text" list="cities" id="city" name="city">
 
  <datalist id="cities">
    <option value="New York City"></option>
    <option value="Tokyo"></option>
    <option value="Barcelona"></option>
    <option value="Mexico City"></option>
```

##### Textarea element

```html
<textarea id="blog" name="blog" rows="5" cols="30">
</textarea>
```

##### Submit Form

```html
<form>
  <input type="submit" value="Send">
</form>
```

#### Validation

##### Requiring an Input

```html
<input id="allergies" name="allergies" type="text" required>
```

##### Checking Text Length

```html
 <input id="summary" name="summary" type="text" minlength="5" maxlength="250" required>
```

# CSS

Internal Stylesheet

```html
<head>
  <style>
    p {
      color: red;
      font-size: 20px;
    }
  </style>
</head>
```

Linking the CSS File

```html
<link href='./style.css' rel='stylesheet'>
```

Universal

```html
* { 
  font-family: Verdana;
}
```

Class

```html
<p class='brand'>Sole Shoe Company</p>

.brand {
 
}
```

Multiple Classes

```html
<h1 class='green bold'> ... </h1>

.green {
  color: green;
}
 
.bold {
  font-weight: bold;
}
```

ID

```html
<h1 id='large-title'> ... </h1>

#large-title {
 
}
```

Attribute

```html
<img src='/images/seasons/cold/winter.jpg'>

img[src*='winter'] {
  height: 50px;
}
```

Pseudo-class

```html
p:hover {
  background-color: lime;
}
```

Descendant Combinator

```html
.description h5 {
  color: blueviolet;
}
```

Multiple Selectors

```html
h1, 
.menu {
  font-family: Georgia;
}
```

Font Family (change text style) https://www.cssfontstack.com/

```html
h1 {
  font-family: Garamond;
}
```

Font Size

```html
p {
  font-size: 18px;
}
```

Font Weight

```html
p {
  font-weight: bold;
}
```

Text Align

```html
h1 {
  text-align: right/left/center/justify;
}
```

Color and Background Color

```html
h1 {
  color: red;
  background-color: blue;
}
```

Opacity (0-1)

```html
.overlay {
  opacity: 0.5;
}
```

Background Image

```html
.main-banner {
  background-image: url('https://www.example.com/image.jpg');
}
```

```html
.main-banner {html
  background-image: url('images/mountains.jpg');
}
```

Important

The !important flag will override any style, however it should almost never be used, as it is extremely difficult to override.

```html
p {
  color: blue !important;
}
```

#### Box Model

![test](diagram-boxmodel.svg)

##### Height and Width

```html
p {
  height: 80px;
  width: 240px;
}
```

##### Borders

A *border* is a line that surrounds an element, like a frame around a painting. Borders can be set with a specific `width`, `style`, and `color`:

- `width`—The thickness of the border. A border’s thickness can be set in pixels or with one of the following keywords: `thin`, `medium`, or `thick`.
- `style`—The design of the border. Web browsers can render any of [10 different styles](https://developer.mozilla.org/en-US/docs/Web/CSS/border-style#Values). Some of these styles include: `none`, `dotted`, and `solid`.
- `color`—The color of the border. Web browsers can render colors using a few different formats, including [140 built-in color keywords](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value).

```html
p {
  border: 3px solid coral;
}
```

##### Border Radius

```html
div.container {
  border: 3px solid blue;
  border-radius: 5px or 50%;
}
```

##### Padding

The code in this example puts 10 pixels of space between the content of the paragraph (the text) and the borders, on all four sides.

The `padding` property is often used to expand the background color and make the content look less cramped.

If you want to be more specific about the amount of padding on each side of a box’s content, you can use the following properties:

- `padding-top`
- `padding-right`
- `padding-bottom`
- `padding-left`

```html
p.content-header {
  border: 3px solid coral;
  padding: 10px;
}
```

##### Padding Shorthand

In the example above, the four values `6px 11px 4px 9px` correspond to the amount of padding on each side, in a clockwise rotation. In order, it specifies the padding-top value (`6px`), the padding-right value (`11px`), the padding-bottom value (`4px`), and the padding-left value (`9px`) of the content

```html
p.content-header {
  padding: 6px 11px 4px 9px;
}
```

##### Margin

The code in the example will place 20 pixels of space on the outside of the paragraph’s box on all four sides. This means that other HTML elements on the page cannot come within 20 pixels of the paragraph’s border.

If you want to be even more specific about the amount of margin on each side of a box, you can use the following properties:

- `margin-top`
- `margin-right`
- `margin-bottom`
- `margin-left`

```html
p {
  border: 1px solid aquamarine;
  margin: 20px;
}
```

##### Margin Shorthand

```html
p {
  margin: 6px 10px 5px 12px;
}
```

##### Minimum and Maximum Height and Width

```html
p {
  min-width: 300px;
  max-width: 600px;
}

p {
  min-height: 150px;
  max-height: 300px;
}
```

##### Overflow

The `overflow` property controls what happens to content that spills, or overflows, outside its box. The most commonly used values are:

- `hidden`—when set to this value, any content that overflows will be hidden from view.

- `scroll`—when set to this value, a scrollbar will be added to the element’s box so that the rest of the content can be viewed by scrolling.

- `visible`—when set to this value, the overflow content will be displayed outside of the containing element. Note, this is the default value.

  For a more in-depth look at `overflow`, including additional properties like `overflow-x` and `overflow-y` that separate out the horizontal and vertical values, head over to the MDN [documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/overflow).

```html
p {
  overflow: scroll; 
}
```

##### Resetting Defaults

User agent stylesheets often have default CSS rules that set default values for padding and margin. This affects how the browser displays HTML elements, which can make it difficult for a developer to design or style a web page.

Many developers choose to reset these default values so that they can truly work with a clean slate.

```html
* {
  margin: 0;
  padding: 0;
}
```

##### Visibility

Elements can be hidden from view with the `visibility` property.

**Note:** What’s the difference between `display: none` and `visibility: hidden`? An element with `display: none` will be completely removed from the web page. An element with `visibility: hidden`, however, will not be visible on the web page, but the space reserved for it will.

The `visibility` property can be set to one of the following values:

- `hidden` — hides an element.
- `visible` — displays an element.
- `collapse` — collapses an element.

```html
.future {
  visibility: hidden;
}
```

#### Box Model: Content-Box

##### Position: Relative

In the example above, the element of `green-box` class will be moved down 50 pixels, and to the right 120 pixels, from its default static position. The image below displays the new position of the box.

```html
.green-box {
  background-color: green;
  position: relative;
  top: 50px;
  left: 120px;
}
```

This is done by accompanying the `position` declaration with one or more of the following *offset properties* that will move the element away from its default static position:

- `top` - moves the element down from the top.
- `bottom` - moves the element up from the bottom.
- `left` - moves the element away from the left side (to the right).
- `right` - moves the element away from the right side (to the left).

##### Position: Absolute

Another way of modifying the position of an element is by setting its position to `absolute`.

When an element’s position is set to `absolute`, all other elements on the page will ignore the element and act like it is not present on the page. The element will be positioned relative to its closest positioned parent element, while offset properties can be used to determine the final position from there. Take a look at the image below:

##### Position: Fixed

We can *fix* an element to a specific position on the page (regardless of user scrolling) by setting its position to `fixed`, and accompanying it with the familiar offset properties `top`, `bottom`, `left`, and `right`.

```html
.title {
  position: fixed;
  top: 0px;
  left: 0px;
}
```

##### Position: Sticky

The `sticky` value is another position value that keeps an element in the document flow as the user scrolls, but *sticks* to a specified position as the page is scrolled further. This is done by using the `sticky` value along with the familiar offset properties, as well as one new one.

```html
.box-bottom {
  background-color: darkgreen;
  position: sticky;
  top: 240px;
}
```

##### Z-Index

```html
.blue-box {
  background-color: blue;
  position: relative;
  z-index: 1;
}
 
.green-box {
  background-color: green;
  position: relative;
  top: -170px;
  left: 170px;
}
```

In the example above, we set the `.blue-box` position to `relative` and the z-index to 1. We changed position to `relative`, because the `z-index` property does *not* work on static elements. The z-index of `1` moves the `.blue-box` element forward, because the `z-index` value has not been explicitly specified for the `.green-box` element, which means it has a default `z-index` value of 0. 

The `z-index` property controls how far back or how far forward an element should appear on the web page when elements overlap. This can be thought of as the *depth* of elements, with deeper elements appearing behind shallower elements.

The `z-index` property accepts integer values. Depending on their values, the integers instruct the browser on the order in which elements should be layered on the web page.

#### Display

##### Inline Display

The default `display` for some elements, such as `<em>`, `<strong>`, and `<a>`, is called *inline*. Inline elements have a box that wraps tightly around their content, only taking up the amount of space necessary to display their content and not requiring a new line after each element. The height and width of these elements cannot be specified in the CSS document. For example, the text of an anchor tag (`<a>`) will, by default, be displayed on the same line as the surrounding text, and it will only be as wide as necessary to contain its content. `inline` elements cannot be altered in size with the `height` or `width` CSS properties.

```html
To learn more about <em>inline</em> elements, read <a href="#">MDN documentation</a>. 
```

```html
h1 {
  display: inline;
}
```

##### Display: Block

Some elements are not displayed in the same line as the content around them. These are called *block-level* elements. These elements fill the entire width of the page by default, but their `width` property can also be set. Unless otherwise specified, they are the height necessary to accommodate their content.

Elements that are block-level by default include all levels of heading elements (`<h1>` through `<h6>`), `<p>`, `<div>` and `<footer>`. For a complete list of block level elements, visit [the MDN documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements).

##### Display: Inline-Block

The third value for the `display` property is `inline-block`. Inline-block display combines features of both inline and block elements. Inline-block elements can appear next to each other and we can specify their dimensions using the `width` and `height` properties. Images are the best example of default inline-block elements.

Let’s take a look at the code:

```html
<div class="rectangle">
  <p>I’m a rectangle!</p>
</div>
<div class="rectangle">
  <p>So am I!</p>
</div>
<div class="rectangle">
  <p>Me three!</p>
</div>
```

```html
.rectangle {
  display: inline-block;
  width: 200px;
  height: 300px;
}
```

There are three rectangular divs that each contain a paragraph of text. The `.rectangle` `<div>`s will all appear inline (provided there is enough space from left to right) with a width of 200 pixels and height of 300 pixels, even though the text inside of them may not require 200 pixels by 300 pixels of space.

##### Float

The `float` property is commonly used for wrapping text around an image while moving elements left and right for layout purposes is better left to tools like CSS grid and flexbox, which you’ll learn about later on.

The `float` property is often set using one of the values below:

- `left` - moves, or floats, elements as far left as possible.
- `right` - moves elements as far right as possible.

```html
.green-section {
  width: 50%;
  height: 150px;
}
 
.orange-section {
  background-color: orange;
  width: 50%;
  float: right;
}
```



