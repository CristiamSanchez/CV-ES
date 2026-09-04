(function () {
    const body = document.body;
    const themeToggle = document.querySelector("[data-theme-toggle]");
    const sections = document.querySelectorAll(".resume-section");
    const navigationLinks = document.querySelectorAll(".nav-link[href^='#']");
    const brandLink = document.querySelector(".top-nav-brand");
    const profileImage = document.querySelector(".hero-photo");
    const backToTop = document.querySelector("[data-back-to-top]");
    const langToggle = document.querySelector("[data-lang-toggle]");
    const langToggleLabel = document.querySelector("[data-lang-toggle-label]");
    const i18nElements = document.querySelectorAll("[data-i18n]");
    const sectionMap = new Map(Array.from(sections).map(function (section) {
        return [section.id, section];
    }));

    if (profileImage) {
        profileImage.addEventListener("error", function () {
            const fallback = document.createElement("span");
            fallback.className = "hero-photo-fallback";
            fallback.setAttribute("aria-label", "Cristiam Sanchez");
            fallback.textContent = "CS";
            profileImage.replaceWith(fallback);
        }, { once: true });
    }

    function setTheme(isDark) {
        body.classList.toggle("dark-mode", isDark);
        themeToggle.setAttribute("aria-pressed", String(isDark));
        themeToggle.setAttribute("aria-label", isDark ? "Activar modo claro" : "Activar modo oscuro");
        themeToggle.innerHTML = isDark ? '<i class="fas fa-sun" aria-hidden="true"></i>' : '<i class="fas fa-moon" aria-hidden="true"></i>';
    }

    if (themeToggle) {
        setTheme(localStorage.getItem("cv-theme") === "dark");
        themeToggle.addEventListener("click", function () {
            const isDark = !body.classList.contains("dark-mode");
            setTheme(isDark);
            localStorage.setItem("cv-theme", isDark ? "dark" : "light");
        });
    }

    function selectSection(sectionId, updateHistory) {
        const selectedSection = sectionMap.get(sectionId) || sectionMap.get("sobre-mi");
        const selectedId = selectedSection.id;

        sections.forEach(function (section) {
            section.classList.toggle("is-selected", section === selectedSection);
            section.classList.toggle("is-visible", section === selectedSection);
        });

        navigationLinks.forEach(function (link) {
            const isActive = link.getAttribute("href") === "#" + selectedId;
            link.classList.toggle("is-active", isActive);
            link.setAttribute("aria-current", isActive ? "page" : "false");
        });

        body.classList.add("view-ready");
        if (updateHistory) {
            window.history.pushState({ sectionId: selectedId }, "", "#" + selectedId);
        }
        window.scrollTo({ top: 0, behavior: "smooth" });
    }

    navigationLinks.forEach(function (link) {
        link.addEventListener("click", function (event) {
            event.preventDefault();
            selectSection(link.getAttribute("href").slice(1), true);
        });
    });

    if (brandLink) {
        brandLink.addEventListener("click", function (event) {
            event.preventDefault();
            selectSection("sobre-mi", true);
        });
    }

    window.addEventListener("popstate", function () {
        selectSection(window.location.hash.slice(1), false);
    });

    selectSection(window.location.hash.slice(1) || "sobre-mi", false);

    function updateScrollProgress() {
        const scrollableHeight = document.documentElement.scrollHeight - window.innerHeight;
        const progress = scrollableHeight > 0 ? window.scrollY / scrollableHeight : 0;
        body.style.setProperty("--scroll-progress", progress);
        body.classList.toggle("is-scrolling", window.scrollY > 8);
        if (backToTop) {
            backToTop.classList.toggle("is-visible", window.scrollY > 120);
        }
    }

    updateScrollProgress();
    window.addEventListener("scroll", updateScrollProgress, { passive: true });

    if (backToTop) {
        backToTop.addEventListener("click", function (event) {
            event.preventDefault();
            selectSection("sobre-mi", true);
        });
    }

    // ---------------------------------------------------------------
    // Selector de idioma (ES / EN)
    // ---------------------------------------------------------------
    const translations = {
        en: {
            "nav.perfil": "Profile",
            "nav.experiencia": "Experience",
            "nav.educacion": "Education",
            "nav.habilidades": "Skills",
            "nav.proyectos": "Projects",
            "nav.certificaciones": "Certifications",
            "nav.contacto": "Contact",

            "hero.subheading": "Software Developer · Backend .NET · APIs · SQL Server · PostgreSQL",
            "hero.lead": "IT professional with over 15 years of experience in software development and systems analysis. Mainly experienced with C#, ASP.NET, SQL Server and enterprise application development. Currently focused on strengthening backend development with ASP.NET Core, Web APIs, Entity Framework Core, software architecture, Docker, automated testing and CI/CD practices.",
            "hero.download": "Download CV (PDF)",

            "exp.h2": "Professional Experience",
            "exp.job1.title": "Software Developer",
            "exp.job1.desc": "Development and maintenance of internal applications using C# and SQL Server. Development and validation of REST APIs with ASP.NET, including endpoint integration and testing before production deployments. Directly involved in stabilizing critical internal bank processes, reducing user-reported incidents.",
            "exp.job1.date": "May 2023 - Present",
            "exp.job2.title": "Systems Analyst / Technical Support",
            "exp.job2.desc": "Development of web applications and technical support for institutional users.",
            "exp.job2.date": "April 2022 - March 2023",
            "exp.job3.title": "Systems Developer",
            "exp.job3.desc": "Development of payroll systems using C# and SQL Server. Development and consumption of web services using JSON and VB.",
            "exp.job3.date": "November 2019 - October 2020",
            "exp.job4.title": "Technology Analyst",
            "exp.job4.desc": "Development and maintenance of systems with C# and SQL Server. Analysis, collection and preparation of statistical information.",
            "exp.job4.date": "April 2013 - January 2017",
            "exp.job5.title": "Programmer Analyst",
            "exp.job5.desc": "Development of enterprise systems using C# and SQL Server.",
            "exp.job5.date": "August 2011 - January 2012",

            "edu.h2": "Academic Background",
            "edu.ceutec.degree1": "Computer Engineering",
            "edu.ceutec.degree2": "University Technician in Information Systems Development",
            "edu.ceutec.degree3": "Logistics Management Engineering",
            "edu.byu.title": "Technology and development training",
            "edu.byu.desc": "Courses related to programming, web fundamentals, frontend and databases.",
            "edu.byu.date": "2021 - Present",

            "skills.h2": "Technical Skills",
            "skills.backend": "Backend Development",
            "skills.databases": "Databases",
            "skills.frontend": "Frontend",
            "skills.devops": "DevOps & Tools",
            "skills.quality": "Software Quality",
            "skills.main-tech": "Core Technologies",

            "proj.h2": "Development Projects",
            "proj.intro": "A selection of projects showcasing hands-on experience in backend, APIs, databases, architecture, testing and DevOps.",
            "proj.p1.desc": "Web API built with ASP.NET Core, layered architecture, PostgreSQL and Entity Framework Core. Includes JWT, Docker, unit/integration testing and CI/CD.",
            "proj.p2.desc": "REST API with ASP.NET Core, Clean Architecture and CQRS. Implements JWT authentication, SQL Server, Docker and automated testing.",
            "proj.p3.desc": "Application focused on ticket management and operational workflows, with an emphasis on backend and process organization.",
            "proj.p4.desc": "CRUD application for managing phone extensions.",
            "proj.p5.desc": "Web system for expense report management using Web Forms, C#, SQL Server and stored procedures.",
            "proj.p6.desc": "Frontend project integrated with a .NET Core and PostgreSQL API, using modern web development technologies.",

            "cert.h2": "Certifications & Additional Training",

            "contact.h2": "Contact",
            "contact.email": "Email:",
            "contact.linkedin-label": "LinkedIn Profile"
        }
    };

    function applyLanguage(lang) {
        if (lang === "en") {
            i18nElements.forEach(function (el) {
                const key = el.getAttribute("data-i18n");
                const value = translations.en[key];
                if (value) {
                    el.textContent = value;
                }
            });
            document.documentElement.setAttribute("lang", "en");
            if (langToggleLabel) langToggleLabel.textContent = "ES";
            if (langToggle) langToggle.setAttribute("aria-label", "Cambiar a Español");
        } else {
            i18nElements.forEach(function (el) {
                if (el.dataset.esOriginal) {
                    el.textContent = el.dataset.esOriginal;
                }
            });
            document.documentElement.setAttribute("lang", "es");
            if (langToggleLabel) langToggleLabel.textContent = "EN";
            if (langToggle) langToggle.setAttribute("aria-label", "Switch to English");
        }
    }

    // Guarda el texto original en español antes de cualquier cambio
    i18nElements.forEach(function (el) {
        el.dataset.esOriginal = el.textContent.trim().replace(/\s+/g, " ");
    });

    if (langToggle) {
        const savedLang = localStorage.getItem("cv-lang") || "es";
        applyLanguage(savedLang);

        langToggle.addEventListener("click", function () {
            const currentLang = document.documentElement.getAttribute("lang") === "en" ? "en" : "es";
            const nextLang = currentLang === "en" ? "es" : "en";
            applyLanguage(nextLang);
            localStorage.setItem("cv-lang", nextLang);
        });
    }

})();
