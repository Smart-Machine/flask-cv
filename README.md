### How to run
> ```bash
> docker compose up
> ```

### Basic JSON REST API
> Contact
> ```bash
> curl http://0.0.0.0:5000/v1/contact 
> ```
> ---
> ```json
> {
>   "address": "Chisinau, Moldova",
>   "email": "radu.calin500@gmail.com",
>   "github": "github.com/Smart-Machine",
>   "phone": "+373 60057214"
> } 
> ```
> ---

> Education
> ```bash
> curl http://0.0.0.0:5000/v1/education
> ```
> ---
> ```json
>{
>  " - 06/2025": {
>    "details": [
>      "Software Engineering Bachelor Degree, that includes several branches of math, theory based computer science, and much more. The speciality of this degree is the PBL (Project Base Learning), thus most of the acquired knowledge are the result of a finished project."
>    ],
>    "place": "The Technical University of Moldova",
>    "pursued": "Bachelor of Science in Software Engineering"
>  },
>  "01/2023 - 01/2023": {
>    "details": [
>      "Use reusable components to render views where data changes over time",
>      "Organize React projects to create more scalable and maintainable websites and apps",
>      "Use props to pass data between components. Create dynamic and interactive web pages and apps",
>      "Use forms to allow users to interact with the app. Build an application in React"
>    ],
>    "place": "Coursera",
>    "pursued": "React Basics Certificate"
>  },
>  "01/2023 - 1/2023": {
>    "details": [
>      "Creating simple JavaScript codes.",
>      "Creating and manipulating objects and arrays.",
>      "Writing unit tests using Jest."
>    ],
>    "place": "Coursera",
>    "pursued": "Programming with JavaScript Certificate"
>  },
>  "02/2023 - 02/2023": {
>    "details": [
>      "Create robust and reusable components with advanced techniques and learn different patterns to reuse common behavior.",
>      "Interact with a remote server and fetch and post data via an API",
>      "Seamlessly test React applications with React Testing Library.",
>      "Integrate commonly used React libraries to streamline your application development"
>    ],
>    "place": "Coursera",
>    "pursued": "Advanced React Certificate"
>  }
>}
>
>
> ---

> Experience
> ```bash
> curl http://0.0.0.0:5000/v1/experience
> ```
> --- 
> ```json
> {
>     "02/2021 \u2013 02/2022": {
>       "achievements": [
>         "Developed a low-level, simplified reverse proxy for medical device farm, as a replacement for Nginx",
>         "Participated in the migration of UI, from a static HTML to responsive React, for the medical device farm.",
>         "Participated in the development of web-socket architecture and migration for the medical device farm."
>       ],
>       "company": "SmartSoftDev",
>       "tech": [
>         "C++",
>         "Python",
>         "React",
>         "Bash"
>       ],
>       "title": "Software Engineer"
>     },
>     "03/2022 \u2013 04/2024": {
>       "achievements": [
>         "Developed and maintained a collection of web scrapers.",
>         "Introduced major changes into the project, like the integration of a modern headless browser replacing dozens of deprecated dependencies, which halved the time for developing a data miner.",
>         "During my last year of work, a coverage of 99.8% of data was achieved due to the radical changes brought in the project, which was the highest score ever reached in the company."
>       ],
>       "company": "CIAL Dun & Bradstreet",
>       "tech": [
>         "Python",
>         "Scrapy",
>         "Docker",
>         "Playwright",
>         "Redis",
>         "MongoDB",
>         "Splash",
>         "Javascript",
>         "Bash"
>       ],
>       "title": "Software Developer"
>     },
>     "04/2020 \u2013 02/2021": {
>       "achievements": [
>         "Participated in the server-side development of a warehouse management system",
>         "Managed enpoints, developed the RBAC system, managed database"
>       ],
>       "company": "Light Square Development",
>       "tech": [
>         "Golang",
>         "PostgreSQL"
>       ],
>       "title": "Backend Developer"
>     },
>     "05/2024 \u2013 present": {
>       "achievements": [
>         "Participate in the migration of monolithic product, called 999 written in Python 2.3, towards microservices in Golang.",
>         "Maintaining the big monolithic product, called 999.md"
>       ],
>       "company": "Simpals",
>       "tech": [
>         "Tornado",
>         "ElasticSearch",
>         "MongoDB",
>         "Python",
>         "Golang",
>         "gRPC",
>         "GraphQL",
>         "Redis",
>         "Docker"
>       ],
>       "title": "Middle Backend Developer"
>     }
> }
>```
> ---

> Languages 
>```bash
> curl http://0.0.0.0:5000/v1/languages
> ```
> ---
> ```json
>{
>  "English": "C1",
>  "German": "A1",
>  "Romaninan": "native",
>  "Russian": "native"
>}
> ```
> ---

> Skills
> ```bash
> curl http://0.0.0.0:5000/v1/skills
>```
> ---
> ```json
>{
>  "skills": {
>    "languages": [
>      "Python",
>      "JavaScript",
>      "Go",
>      "C++",
>      "SQL",
>      "Bash"
>    ],
>    "technologies": [
>      "Docker",
>      "Linux",
>      "React",
>      "Scrapy",
>      "Playwright",
>      "REST",
>      "gRPC",
>      "RabbitMQ",
>      "Websockets"
>    ]
>  }
>}
> ---

> Summary
> ```bash
> curl http://0.0.0.0:5000/v1/summary
>```
> ---
> ```json
> {
>    "summary": "Experienced software developer with a passion forcreating smart solutions and optimizing performance.Equipped with a solid foundation in software engineering principles, I flourish in dynamic environments where creativity meets technical precision."
> }
> ```
>  ---

### Issues
* The Flask CLI stopped working with the addition of the unicorn & nginx. 
* Test coverage must be added in the future.
* Configuring CORS for the swagger on the Nginx.
* Adding extra features, like rate-limit, caching, etc.