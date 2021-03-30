function(modal) {
    modal.respond('fontsizeChosen', '{{ feature_name }}', ['{{ all_feature_names|join:"','" }}']);
    modal.close();
}