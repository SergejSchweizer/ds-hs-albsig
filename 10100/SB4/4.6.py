

#4.1


library(ggplot2)

df_avg <- read.csv2("Downloads/ds-hs-albsig/10100/SB3/avg.csv",sep=",")



df_mw <- read.csv2("Downloads/ds-hs-albsig/10100/SB3/mw.csv",sep=",")


df_pr <- read.csv2("Downloads/ds-hs-albsig/10100/SB3/pr.csv",sep=",")


df_st <- read.csv2("Downloads/ds-hs-albsig/10100/SB3/st.csv",sep=",")


df_hzb <- read.csv2("Downloads/ds-hs-albsig/10100/SB3/hzb.csv",sep=",")



df_all <- merge(df_avg, df_mw, by="mtknr")


df_all <- merge(df_all, df_pr, by="mtknr")


df_all <- merge(df_all, df_st, by="mtknr")


df_all <- merge(df_all, df_hzb, by="mtknr")


df_all["geschl"] <- as.numeric(df$geschl)

# Durschnitsnote
ggplot(data=df_all)+
geom_histogram(mapping=aes(x=avg),binwidth=1)

# Geschlecht
df_all_aggby_geschl <- aggregate(geschl ~ mtknr, df_all, unique )


ggplot(data=df_all_aggby_geschl)+

geom_bar(mapping=aes(x=geschl,fill=geschl))

# aktuelles Semester
df_all_aggby_sem <- aggregate(sem ~ mtknr, df_all, max)


ggplot(data=df_all_aggby_sem)+

geom_histogram(mapping=aes(x=sem),binwidth=1)