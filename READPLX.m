%%
%ketamine
fn = 'D:\sleep24\21Q2\sysD\Thy1-GCaMP6s-M6-K-airpuff-0720.plx';
data = readPLXFileC(fn, 'continuous', 'events');

% M1
eeg1_ch = 2;
% eeg2_ch = 12;
emg1_ch = 4;
emg2_ch = 8;
 sync_ch1 = 1;
sync_ch2 = 2;
eeg1 = double(data.ContinuousChannels(eeg1_ch+64).Values);
% eeg2 = double(data.ContinuousChannels(eeg2_ch+64).Values);
emg1 = double(data.ContinuousChannels(emg1_ch+64).Values);
emg2 = double(data.ContinuousChannels(emg2_ch+64).Values);
emg = emg1 - emg2;
sync1 = double(data.EventChannels(sync_ch1).Timestamps)/data.ADFrequency;
sync2 = double(data.EventChannels(sync_ch2).Timestamps)/data.ADFrequency;