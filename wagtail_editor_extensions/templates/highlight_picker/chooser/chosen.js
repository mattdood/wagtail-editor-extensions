function(modal) {
    modal.respond('highlightChosen', '{{ feature_name }}', ['{{ all_feature_names|join:"','" }}']);
    modal.close();
}