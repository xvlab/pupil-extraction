figure;
subplot(3,1,1)
imagesc(pupilArea70Accumulate');title("小鼠瞳孔面积的变化");
subplot(3,1,2)
imagesc(pupilX70Accumulate');title("小鼠瞳孔水平方向的偏移");
subplot(3,1,3)
imagesc(pupilY70Accumulate');title("小鼠瞳孔竖直方向的偏移");
h=colorbar;
set(h,'Position', [0.925 0.14 0.012 0.72]); 
sgtitle('吹气强度70');
figure;
subplot(3,1,1)
imagesc(pupilArea75Accumulate');title("小鼠瞳孔面积的变化");
subplot(3,1,2)
imagesc(pupilX75Accumulate');title("小鼠瞳孔水平方向的偏移");
subplot(3,1,3)
imagesc(pupilY75Accumulate');title("小鼠瞳孔竖直方向的偏移");
h=colorbar;
set(h,'Position', [0.925 0.14 0.012 0.72]); 
sgtitle('吹气强度75');
figure;
subplot(3,1,1)
imagesc(pupilArea80Accumulate');title("小鼠瞳孔面积的变化");
subplot(3,1,2)
imagesc(pupilX80Accumulate');title("小鼠瞳孔水平方向的偏移");
subplot(3,1,3)
imagesc(pupilY80Accumulate');title("小鼠瞳孔竖直方向的偏移");
h=colorbar;
set(h,'Position', [0.925 0.14 0.012 0.72]); 
sgtitle('吹气强度80');
figure;
subplot(3,1,1)
imagesc(pupilArea85Accumulate');title("小鼠瞳孔面积的变化");
subplot(3,1,2)
imagesc(pupilX85Accumulate');title("小鼠瞳孔水平方向的偏移");
subplot(3,1,3)
imagesc(pupilY85Accumulate');title("小鼠瞳孔竖直方向的偏移");
h=colorbar;
set(h,'Position', [0.925 0.14 0.012 0.72]); 
sgtitle('吹气强度85');