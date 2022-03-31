class Program{

    public Interface IBlock{
        byte[] Data { get; }
        byte[] Hash { get; set; }
        int Nonce { get; set; }
        byte[] PrevHash { get; set; }
        DateTime TimeStamp { get; }
    }


    public class Block : IBlock
    {
        public byte[] Data { get; }
        public byte[] Hash { get; set; }
        public int Nonce { get; set; }
        public byte[] PrevHash { get; set; }
        public DateTime TimeStamp { get; }
    
        public override string ToString()
        {
            return $"{BitCoverter.ToString(Hash).Replace("-","")}:\{BitConverter.ToString(PrevHash).Replace("-","")}"\n {Nonce} {TimeStamp};
        }
    }

    public class BlockChain : IEnumerable<IBlock>
    {
        
    }

    static void Main(string[] args)
    {

    }

}