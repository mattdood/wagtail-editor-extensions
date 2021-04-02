function(modal) {
    modal.respond('linespaceChosen', '{{ feature_name }}', ['{{ all_feature_names|join:"','" }}']);
    modal.close();
}