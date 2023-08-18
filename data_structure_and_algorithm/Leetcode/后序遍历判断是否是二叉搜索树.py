# def is_bst_postorder(postorder):
#     if not postorder:
#         return False
#     root = postorder[-1]
#     left_subtree = []
#     right_subtree = []
    
#     split_index = 0
#     for i in range(len(postorder)-1):
#         if postorder[i] < root:
#             left_subtree.append(postorder[i])
#         else:
#             split_index = i
#             break
#     # 检查右子树是否都大于根节点的值(原postorder的最后一个值已经作为根节点了)
#     for i in range(split_index, len(postorder) - 1):
#         if postorder[i] < root:
#             return False
#         right_subtree.append(postorder[i])
#     left_is_bst = is_bst_postorder(left_subtree)
#     right_is_bst = is_bst_postorder(right_subtree)
    
#     return left_is_bst and right_is_bst

# print(is_bst_postorder([5, 7, 6, 9, 11, 10, 8]))
def is_bst_postorder(postorder):
    if not postorder:
        return False

    root = postorder[-1]
    left_subtree = []
    right_subtree = []

    # 找到左子树和右子树的分界点
    split_index = 0
    for i in range(len(postorder) - 1):
        if postorder[i] < root:
            left_subtree.append(postorder[i])
        else:
            split_index = i
            break

    # 检查右子树是否都大于根节点的值
    for i in range(split_index, len(postorder) - 1):
        if postorder[i] < root:
            return False
        right_subtree.append(postorder[i])

    # 递归检查左子树和右子树是否也是二叉查找树的后序遍历结果
    left_is_bst = True
    right_is_bst = True

    if left_subtree:
        left_is_bst = is_bst_postorder(left_subtree)
    if right_subtree:
        right_is_bst = is_bst_postorder(right_subtree)

    return left_is_bst and right_is_bst


# 示例测试
postorder_sequence = [5, 7, 6, 9, 11, 10, 8]
if is_bst_postorder(postorder_sequence):
    print("该序列是二叉查找树的后序遍历结果。")
else:
    print("该序列不是二叉查找树的后序遍历结果。")
 