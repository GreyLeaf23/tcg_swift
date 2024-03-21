# TCG Swift - Into The Action!

A learning experience to swiftly enjoy the world of trading card games!

![TCG](https://github.com/GreyLeaf23/tcg_swift/blob/master/tcg-swift/front-end/assets/images/TCG_Swift_Logo.png)

## Motivation


One thing that everything seems to have in common is the rapid change that everything is going under, and card games are no exception.
With so many concepts and mechanics being release, is difficult for players to keep up with all the jargon that the game brings, especially for newer players.

It feels like you're studying the game instead of.... PLAYING IT.

This is the reasoning of creating an experience that allows players to enjoy all the richness that trading card games have to offer, for anyone
of any age and skill!

Test out the actual website here at [tcgswift.click](http://tcgswift.click) and checkout the blogpost made for this project here: [Blog Post](https://www.linkedin.com/pulse/tcg-swift-giovanni-y-carmona-9rqbe).


## Build status



[![Build Status](https://travis-ci.org/akashnimare/foco.svg?branch=master)](https://travis-ci.org/akashnimare/foco)
[![Windows Build Status](https://ci.appveyor.com/api/projects/status/github/akashnimare/foco?branch=master&svg=true)](https://ci.appveyor.com/project/akashnimare/foco/branch/master)

## Code style



[![js-standard-style](https://img.shields.io/badge/code%20style-standard-brightgreen.svg?style=flat)](https://github.com/feross/standard)

## Screenshots
![Landing Page](https://github.com/GreyLeaf23/tcg_swift/tcg-swift/front-end/assets/images/screenshots/main-page.png)
![Guide Page](https://github.com/GreyLeaf23/tcg_swift/tcg-swift/front-end/assets/images/screenshots/guide.png)
![Deck Builder Page](https://github.com/GreyLeaf23/tcg_swift/tcg-swift/front-end/assets/images/screenshots/deck-builder.png)
![Outside Sources Page](https://github.com/GreyLeaf23/tcg_swift/blob/master/tcg-swift/front-end/assets/images/screenshots/outside-sources.png)


## Tech/framework used

<b>Built with</b>
- [Python](https://www.python.org/)
- [Javascript](https://www.javascript.com/)
- [MySQL](https://www.mysql.com/)
- [HTML](https://html.com/)
- [CSS](https://cssprofile.collegeboard.org/)

## Features
What makes your project stand out?

## Code Example

All of the shown examples are snippets of the code architecture:

**HTML** -
```html
<div class="header-bottom skewBg" data-header>
            <div class="container">

                <a href="#" class="logo">TCG SWIFT</a>

                <nav class="navbar" data-navbar>
                    <ul class="navbar-list">

                        <li class="navbar-item">
                            <a href="#home" class="navbar-link skewBg" data-nav-link>Home</a>
                        </li>

                        <li class="navbar-item">
                            <a href="#features" class="navbar-link skewBg" data-nav-link>Features</a>
                        </li>

                        <li class="navbar-item">
                            <a href="#swift" class="navbar-link skewBg" data-nav-link>Swift</a>
                        </li>

                        <li class="navbar-item">
                            <a href="#decks" class="navbar-link skewBg" data-nav-link>Decks</a>
                        </li>

                        <li class="navbar-item">
                            <a href="#players" class="navbar-link skewBg" data-nav-link>Players</a>
                        </li>

                        <li class="navbar-item">
                            <a href="#blog" class="navbar-link skewBg" data-nav-link>Blog</a>
                        </li>

                        <li class="navbar-item">
                            <a href="#" class="navbar-link skewBg" data-nav-link>Contact</a>
                        </li>

                    </ul>
                </nav>

                <div class="header-actions">

                    <button class="search-btn" aria-label="open search" data-search-toggler>
                        <ion-icon name="search-outline"></ion-icon>
                    </button>

                    <button class="nav-toggle-btn" aria-label="toggle menu" data-nav-toggler>
                        <ion-icon name="menu-outline" class="menu"></ion-icon>
                        <ion-icon name="close-outline" class="close"></ion-icon>
                    </button>

                </div>

            </div>
        </div>

    </header>
```

**CSS** -
```css
/*-----------------------------------*\
  #CUSTOM PROPERTY
\*-----------------------------------*/

:root {

  /**
   * colors
   */

  --rich-black-fogra-29_95: hsla(222, 18%, 11%, 0.95);
  --raisin-black-1: hsl(0, 0%, 16%);
  --raisin-black-2: hsl(236, 17%, 17%);
  --raisin-black-3: hsl(280, 11%, 11%);
  --raisin-black-4: hsl(280, 8%, 15%);
  --english-violet: hsl(274, 21%, 23%);
  --eerie-black-1: hsl(277, 25%, 10%);
  --eerie-black-2: hsl(280, 7%, 8%);
  --roman-silver: hsl(220, 6%, 59%);
  --quick-silver: hsl(0, 1%, 65%);
  --light-gray-1: hsl(0, 0%, 80%);
  --light-gray-2: hsl(0, 2%, 82%);
  --marigold_75: hsla(42, 99%, 46%, 0.75);
  --xiketic_90: hsla(280, 37%, 8%, 0.9);
  --cultured-2: hsl(0, 0%, 97%);
  --marigold: hsl(42, 99%, 46%);
  --platinum: hsl(0, 0%, 89%);
  --dim-gray: hsl(0, 0%, 42%);
  --white_15: hsla(0, 0%, 100%, 0.15);
  --white_10: hsla(0, 0%, 100%, 0.1);
  --xiketic: hsl(277, 25%, 10%);
  --silver: hsl(0, 0%, 78%);
  --white: hsl(0, 0%, 100%);
  --jet: hsl(236, 13%, 23%);

  /**
   * typography
   */

  --ff-oxanium: 'Oxanium', cursive;
  --ff-poppins: 'Poppins', sans-serif;

  --fs-1: 7rem;
  --fs-2: 4.5rem;
  --fs-3: 3.6rem;
  --fs-4: 2.4rem;
  --fs-5: 2.2rem;
  --fs-6: 2rem;
  --fs-7: 1.6rem;
  --fs-8: 1.5rem;
  --fs-9: 1.4rem;
  --fs-10: 1.3rem;
  --fs-11: 1.2rem;

  --fw-500: 500;
  --fw-600: 600;
  --fw-700: 700;
  --fw-800: 800;

  /**
   * spacing
   */

  --section-padding: 120px;

  /**
   * gradient
   */

  --gradient: radial-gradient(circle, hsl(250, 7%, 17%), hsl(250, 11%, 11%));

  /**
   * box shadow
   */

  --shadow-1: 0px 2px 8px 0px hsla(0, 0%, 0%, 0.2),
              inset 0px 2px 8px 0px hsla(0, 0%, 0%, 0.4);
  --shadow-2: 0px 5px 10px 1px hsla(0, 0%, 0%, 0.4);
  --shadow-3: 0px 5px 10px 1px hsla(219, 98%, 17%, 0.2);
  --shadow-4: 0px 5px 10px 1px hsla(0, 0%, 0%, 0.15);

  /**
   * transition
   */

  --transition: 0.25s ease;
  --cubic-out: cubic-bezier(0.33, 0.85, 0.4, 0.96);

}
```

**JavaScript** -
```javascript
'use strict';



const navbar = document.querySelector("[data-navbar]");
const navbarLinks = document.querySelectorAll("[data-navbar-link]");
const navbarToggler = document.querySelector("[data-navbar-toggler]");

navbarToggler.addEventListener("click", function () {
  navbar.classList.toggle("active");
  this.classList.toggle("active");
});

for (let i = 0; i < navbarLinks.length; i++) {
    navbarLinks[i].addEventListener("click", function () {
        navbar.classList.toggle("active");
        navbarToggler.classList.toggle("active");
    });
}
```



## How to use?



Brief overview of use:

* General understanding of the ruleset.

* Niche mechanics and concepts explained.

* Deck building and synergies.

* Community sharing.


## License

MIT © [Giovanni Carmona]() [Diego Gonzalez]() [Christian Rosario]() [Jose Nieves]()
