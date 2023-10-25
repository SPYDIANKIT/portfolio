function scrollToSection(sectionId) {
    var section = document.getElementById(sectionId);

    if (section) {
        // Calculate the offset of the section relative to the document
        var offset = section.offsetTop;

        // Scroll to the section with smooth behavior
        window.scrollTo({
            top: offset,
            behavior: 'smooth'
        });
    }
}