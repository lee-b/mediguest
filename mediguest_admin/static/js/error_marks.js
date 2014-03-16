/* mark_tabs_with_errors()
 *
 * Highlight tabs which have fields with validation errors.
 *
*/

var seen = false;

function show_tab(tab_id) {
    /* not implemented */
}

function mark_tab_if_errors(idx, tab_label) {
    mark_tab_if_errors.first = true;

    var search_str = "dijit_layout_ContentPane_";

    var tab = jQuery(tab_label).parent();
    var tab_id = tab.attr('id');
    var pane_id_pos = tab_id.lastIndexOf(search_str);
    var pane_id = tab_id.substr(pane_id_pos);

    var pane = jQuery(document).find("#" + pane_id);
    var errors = jQuery(pane).find(".errorlist");

    if (errors.length > 0) {
        jQuery(tab_label).addClass("tab-errors");

        if (mark_tab_if_errors.first) {
            show_tab(tab_id);
            mark_tab_if_errors.first = false;
        }
    }
}

function mark_tabs_with_errors() {
    if (jQuery(document).find(".errornote").length==0) {
        /* no errors to highlight */
        return;
    }

    var doc = jQuery(document);

    var tab_labels = doc.find("span.tabLabel");
    tab_labels.each( mark_tab_if_errors );
}

jQuery(document).ready( mark_tabs_with_errors );

