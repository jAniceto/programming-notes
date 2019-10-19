Title: CSS selectors
Date: 2017-08-15 23:10
Authors: José Aniceto


In CSS, selectors are patterns used to select the element(s) you want to style.

The "CSS" column indicates in which CSS version the property is defined (CSS1, CSS2, or CSS3).

Selector	 | 	Example	 | 	Example description	 | 	CSS
-----	 | 	-----	 | 	-----	 | 	-----
.class	 | 	.intro	 | 	Selects all elements with class="intro"	 | 	1
#id	 | 	#firstname	 | 	Selects the element with id="firstname"	 | 	1
*	 | 	*	 | 	Selects all elements	 | 	2
element	 | 	p	 | 	Selects all&lt;p&gt; elements	 | 	1
element,element	 | 	div, p	 | 	Selects all &lt;div&gt; elements and all &lt;p&gt; elements	 | 	1
element element	 | 	div p	 | 	Selects all &lt;p&gt; elements inside &lt;div&gt; elements	 | 	1
element&gt;element	 | 	div &gt; p	 | 	Selects all &lt;p&gt; elements where the parent is a &lt;div&gt; element	 | 	2
element+element	 | 	div + p	 | 	Selects all &lt;p&gt; elements that are placed immediately after &lt;div&gt; elements	 | 	2
element1~element2	 | 	p ~ ul	 | 	Selects every &lt;ul&gt; element that are preceded by a &lt;p&gt; element	 | 	3
:active	 | 	a:active	 | 	Selects the active link	 | 	1
::after	 | 	p::after	 | 	Insert something after the content of each &lt;p&gt; element	 | 	2
::before	 | 	p::before	 | 	Insert something before the content of each &lt;p&gt; element	 | 	2
:checked	 | 	input:checked	 | 	Selects every checked &lt;input&gt; element	 | 	3
:disabled	 | 	input:disabled	 | 	Selects every disabled &lt;input&gt; element	 | 	3
:empty	 | 	p:empty	 | 	Selects every &lt;p&gt; element that has no children (including text nodes)	 | 	3
:enabled	 | 	input:enabled	 | 	Selects every enabled &lt;input&gt; element	 | 	3
:first-child	 | 	p:first-child	 | 	Selects every &lt;p&gt; element that is the first child of its parent	 | 	2
::first-letter	 | 	p::first-letter	 | 	Selects the first letter of every &lt;p&gt; element	 | 	1
::first-line	 | 	p::first-line	 | 	Selects the first line of every &lt;p&gt; element	 | 	1
:first-of-type	 | 	p:first-of-type	 | 	Selects every &lt;p&gt; element that is the first &lt;p&gt; element of its parent	 | 	3
:focus	 | 	input:focus	 | 	Selects the input element which has focus	 | 	2
:hover	 | 	a:hover	 | 	Selects links on mouse over	 | 	1
:in-range	 | 	input:in-range	 | 	Selects input elements with a value within a specified range	 | 	3
:invalid	 | 	input:invalid	 | 	Selects all input elements with an invalid value	 | 	3
:lang(language)	 | 	p:lang(it)	 | 	Selects every &lt;p&gt; element with a lang attribute equal to "it" (Italian)	 | 	2
:last-child	 | 	p:last-child	 | 	Selects every &lt;p&gt; element that is the last child of its parent	 | 	3
:last-of-type	 | 	p:last-of-type	 | 	Selects every &lt;p&gt; element that is the last &lt;p&gt; element of its parent	 | 	3
:link	 | 	a:link	 | 	Selects all unvisited links	 | 	1
:not(selector)	 | 	:not(p)	 | 	Selects every element that is not a &lt;p&gt; element	 | 	3
:nth-child(n)	 | 	p:nth-child(2)	 | 	Selects every &lt;p&gt; element that is the second child of its parent	 | 	3
:nth-last-child(n)	 | 	p:nth-last-child(2)	 | 	Selects every &lt;p&gt; element that is the second child of its parent, counting from the last child	 | 	3
:nth-last-of-type(n)	 | 	p:nth-last-of-type(2)	 | 	Selects every &lt;p&gt; element that is the second &lt;p&gt; element of its parent, counting from the last child	 | 	3
:nth-of-type(n)	 | 	p:nth-of-type(2)	 | 	Selects every &lt;p&gt; element that is the second &lt;p&gt; element of its parent	 | 	3
:only-of-type	 | 	p:only-of-type	 | 	Selects every &lt;p&gt; element that is the only &lt;p&gt; element of its parent	 | 	3
:only-child	 | 	p:only-child	 | 	Selects every &lt;p&gt; element that is the only child of its parent	 | 	3
:optional	 | 	input:optional	 | 	Selects input elements with no "required" attribute	 | 	3
:out-of-range	 | 	input:out-of-range	 | 	Selects input elements with a value outside a specified range	 | 	3
:read-only	 | 	input:read-only	 | 	Selects input elements with the "readonly" attribute specified	 | 	3
:read-write	 | 	input:read-write	 | 	Selects input elements with the "readonly" attribute NOT specified	 | 	3
:required	 | 	input:required	 | 	Selects input elements with the "required" attribute specified	 | 	3
:root	 | 	:root	 | 	Selects the document's root element	 | 	3
::selection	 | 	::selection	 | 	Selects the portion of an element that is selected by a user	 | 	
:target	 | 	#news:target	 | 	Selects the current active #news element (clicked on a URL containing that anchor name)	 | 	3
:valid	 | 	input:valid	 | 	Selects all input elements with a valid value	 | 	3
:visited	 | 	a:visited	 | 	Selects all visited links	 | 	1

