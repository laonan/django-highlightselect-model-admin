(function ($) {
    $(document).ready(function () {
        let $selectedIds = $('#selected_ids');

        if ( $selectedIds.length ) {
            let ids = $selectedIds.val();
            let idJson = JSON.parse(ids);

            $('.action-select').each(function () {
                let $checkbox = $(this);
                for (let id of idJson) {
                    if ($checkbox.val() === id.toString()) {
                        $checkbox.click();
                    }
                }
            });
        }

    });
})(django.jQuery);