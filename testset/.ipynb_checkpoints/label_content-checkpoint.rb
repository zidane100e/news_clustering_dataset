# copy directory general to general_w_label and then
# edit file name or remove duplicates

#title_label_s = '../general_titles_w_label.txt'
#title_label_s = '../global_titles_w_label.txt'
title_label_s = '../industry_titles_w_label.txt'
#title_label_s = '../stock_titles_w_label.txt'

dic1 = {}
File.open(title_label_s).each_line{ |line|
  next if line.strip == ''
  label, text = line.strip.split(', ', 2)
  dic1[text] = label
}

#dir_s = 'general_w_label'
#dir_s = 'global_w_label'
#dir_s = 'stock_w_label'
dir_s = 'industry_w_label'
files = []
Dir.foreach(dir_s) do |f1_s|
  next if f1_s == '.' or f1_s == '..'
  #puts dir_s + '/' + f1_s
  files << dir_s + '/' + f1_s
end

titles_dic = {}
act = nil # rename or delete
label = nil
title = nil
files.each{ |f1_s|
  File.open(f1_s){ |f1|
    title = f1.readline.strip
    titles_dic[title] ||= 0
    titles_dic[title] += 1
    label = dic1[title]
    #p [label, title]
    if titles_dic[title] == 1
      act = 'rename'
    else
      act = 'delete'
    end
  }
  #p dic1
  if act == 'delete'
    #p ['delete', f1_s, title]
    File.delete(f1_s)
  elsif act == 'rename'
    #p ['rename', f1_s, '  ', label.to_s, f1_s]]
    File.rename(f1_s, f1_s + '_' + label.to_s +  '.txt')
  end
}
