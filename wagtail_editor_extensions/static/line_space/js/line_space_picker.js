const React = window.React;
const EditorState = window.DraftJS.EditorState;
const Modifier = window.DraftJS.Modifier;
const RichUtils = window.DraftJS.RichUtils;

class TextLineSpaceSource extends React.Component {

    constructor(props) {
        super(props);

        this.onChosen = this.onChosen.bind(this);
        this.onClose = this.onClose.bind(this);
    }

    componentDidMount() {
        $(document.body).on('hidden.bs.modal', this.onClose);

        this.workflow = ModalWorkflow({
            url: window.chooserUrls.linespaceChooser,
            onload: LINESPACEPICKER_CHOOSER_MODAL_ONLOAD_HANDLERS,
            responses: {
                colourChosen: this.onChosen
            }
        });
    }

    componentWillUnmount() {

        this.workflow = null;

        $(document.body).off('hidden.bs.modal', this.onClose);
    }

    onChosen(toggledLineSpace, featuredLineSpace) {
        // set the chosen colour, ensuring all other colours are unset
        const { editorState, onComplete } = this.props;
        const selection = editorState.getSelection();

        // Only allow one color to be set at a time for the current selection
        const nextContentState = featuredLineSpace
            .reduce((contentState, line_space) => {
                return Modifier.removeInlineStyle(contentState, selection, line_space)
            }, editorState.getCurrentContent());

        var nextEditorState = EditorState.push(
            editorState,
            nextContentState,
            'change-inline-style'
        );

        const currentStyle = editorState.getCurrentInlineStyle();

        // Unset style override for current color.
        if (selection.isCollapsed()) {
            nextEditorState = currentStyle.reduce((state, line_space) => {
              return RichUtils.toggleInlineStyle(state, line_space);
            }, nextEditorState);
        }

        // If there's a color and it's being toggled on, apply it.
        if (toggledLineSpace && !currentStyle.has(toggledLineSpace)) {
            nextEditorState = RichUtils.toggleInlineStyle(
                nextEditorState,
                toggledLineSpace
            );
        }

        this.workflow.close();

        onComplete(nextEditorState);
    }

    onClose(e) {
        e.preventDefault();
        const { onClose } = this.props;
        onClose();
    }

    render() {
        return null;
    }
}

window.draftail.registerPlugin({
    type: 'TEXTLINESPACE',
    source: TextLineSpaceSource,
});
