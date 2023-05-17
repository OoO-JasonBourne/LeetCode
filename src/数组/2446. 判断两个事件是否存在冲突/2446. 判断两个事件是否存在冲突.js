var haveConflict = function(event1, event2) {
    if(event1[1] < event2[0] || event2[1] < event1[0]) return false;
    return true
};