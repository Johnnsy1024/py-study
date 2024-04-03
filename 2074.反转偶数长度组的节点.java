/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseEvenLengthGroups(ListNode head) {
        // if ((head == null) || (head.next == null)) {
        // return head;
        // }
        ListNode dummy = new ListNode(0, head);
        ListNode cur = head; // cur在每一组子链表遍历的过程中是当前子链表前一组子链表的尾节点
        ListNode pre = dummy;
        int subLinkedListNum = 0; // subLinkedListNum记录当前第几组子链表，此数也是当前子链表的最长长度
        while (cur != null) {
            subLinkedListNum++;
            int cursubLinkListLength = 0; // cursubLinkListLength记录当前子链表的长度
            ListNode explore = cur; // explore节点为当前子链表的向下探索节点（可能为空）
            while (explore != null && cursubLinkListLength < subLinkedListNum) {
                cursubLinkListLength++;
                explore = explore.next;
            } // 通过explore节点探索当前
            if (cursubLinkListLength % 2 == 0) {
                for (int i = 0; i < cursubLinkListLength - 1; ++i) { // 链表反转逻辑
                    ListNode removed = cur.next; // 将当前节点的next节点拿出来
                    cur.next = removed.next;
                    removed.next = pre.next;
                    pre.next = removed;
                }
                // 子链表反转之后，cur指向下一组子链表的prev
                pre = cur;
                cur = cur.next;
            } else {
                for (int i = 0; i < cursubLinkListLength; ++i) {
                    pre = pre.next;
                    cur = cur.next;
                }
            }
        }
        return dummy.next;
    }
}