window.addEventListener('scroll', function () {
    const element = document.getElementById('pidor');
    if (element) {
        const scrollPosition = window.scrollY || window.pageYOffset;
        const maxHeight = 99; // Начальная высота в vh
        const minHeight = 0;  // Полное скрытие
        const initialTop = 60; // Начальное положение top в px (из вашего CSS)

        // Вычисляем общую прокручиваемую высоту
        const documentHeight = document.documentElement.scrollHeight - window.innerHeight;
        const scrollProgress = Math.min(scrollPosition / documentHeight, 1);

        // Вычисляем новую высоту
        let newHeight = maxHeight * (1 - scrollProgress);
        newHeight = Math.max(minHeight, newHeight);

        // Вычисляем на сколько уменьшилась высота (в vh)
        const heightReduction = maxHeight - newHeight;

        // Преобразуем уменьшение высоты из vh в px для смещения top
        const vhToPx = (value) => {
            return (value * window.innerHeight) / 100;
        };

        // Новая позиция top (начальная + уменьшение высоты в px)
        const newTop = initialTop + vhToPx(heightReduction);

        // Применяем изменения
        element.style.top = newTop + 'px';
        element.style.height = newHeight + 'vh';
        

        console.log(`Height: ${newHeight}vh, Top: ${newTop}px`);
    }
});