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

```
<p>This paragraph is a child of the body element</p>
```

##### Line Breaks

```
<br>
```

##### Division

“division” or a container that divides the page into sections. 

```
<div> </div> 
```

##### Main

By using <main> as opposed to a <div> element, screen readers and web browsers are better able to identify that whatever is inside of the tag is the bulk of the content.

```
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

```
<ul>...</ul>
```

Ordered Lists

```
<ol>...</ol>
```

##### Images

```
<img src="image-location.jpg" />
```

##### Image Alts (alternative text)

```
<img src="https://content.codecademy.com/courses/web-101/web101-image_brownbear.jpg" alt="Brown Bear"/>
```

##### Videos

```
<video src="myVideo.mp4" width="320" height="240" controls>
  Video not supported
</video>
```

##### Audio and Attributes

```
<audio controls>
  <source src="https://content.codecademy.com/courses/SemanticHTML/dogBarking.mp3" type="audio/mp3">
</audio>
```

##### Video and Embed (.gif)

```
<video src="coding.mp4" controls>Video not supported</video>
<embed src="download.gif"/>
```

##### Links

```
<a href="https://en.wikipedia.org/wiki/Brown_bear" target="_blank">The Brown Bear</a>
```

##### Linking to Relative Page

```
<a href="./contact.html">Contact</a>
```

##### Linking to Same Page

```
 <ul>
    <li><a href="#introduction">Introduction</a></li>
    <li><a href="#habitat">Habitat</a></li>
    <li><a href="#media">Media</a></li>
  </ul>
```

##### Aside Element 

The Aside Element -  additional information that can enhance another element but isn’t required in order to understand the main content. 

```
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

```
<figure>
  <img src="overwatch.jpg">
  <figcaption>This picture shows characters from Overwatch.</figcaption>
</figure>
```

##### Comments

```
<!-- ______ -->
```

#### TABLE

##### Create a Table

```
<table>...</table>
```

##### Table Rows

```
<tr>...</tr>
```

##### Cell element

```
<td>...</td>
```

##### Table Headings (th)

```
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

```
<td colspan="2">Out of Town</td>
```

##### Spanning Rows (merge)

```
<td rowspan="2">Work</td>
```

##### Table Body

```
<tbody>...</tbody>
```

##### Table Headings

```
<thead>...</thead>
```

##### Table Footer

The footer contains information such as: 

- Contact information 
- Copyright information 
- Terms of use 
- Site Map 
- Reference to top of page links

```
<tfoot>
	<p>Contact me at +1 234 567 8910 </p>
</tfoot>
```

#### FORM

##### Text Input

```
<form action="/example.html" method="POST">
  <input type="text" name="first-text-field">
</form>
```

##### Adding a Label

```
<label for="meal">What do you want to eat?</label>
```

##### Password Input

```
<form>
  <label for="user-password">Password: </label>
  <input type="password" id="user-password" name="user-password">
</form>
```

##### Number Input

```
<form>
  <label for="years"> Years of experience: </label>
  <input id="years" name="years" type="number" step="1">
</form>
```

##### Checkbox Input

```
<input id="cheese" name="topping" type="checkbox" value="cheese">
 <label for="cheese">Cheese</label>
```

##### Radio Button Input

```
<input id="yes" type="radio" name="cheese" value="yes">
```

##### Dropdown list

```
<select id="lunch" name="lunch">
    <option value="pizza">Pizza</option>
    <option value="curry">Curry</option>
    <option value="salad">Salad</option>
```

##### Datalist Input

```
<input type="text" list="cities" id="city" name="city">
 
  <datalist id="cities">
    <option value="New York City"></option>
    <option value="Tokyo"></option>
    <option value="Barcelona"></option>
    <option value="Mexico City"></option>
```

##### Textarea element

```
<textarea id="blog" name="blog" rows="5" cols="30">
  </textarea>
```

##### Submit Form

```
<form>
  <input type="submit" value="Send">
</form>
```

#### Validation

##### Requiring an Input

```
<input id="allergies" name="allergies" type="text" required>
```

##### Checking Text Length

```
 <input id="summary" name="summary" type="text" minlength="5" maxlength="250" required>
```

